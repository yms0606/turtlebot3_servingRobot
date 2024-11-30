import sys
import threading
import rclpy
import matplotlib as mpl
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem, QDialog, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from matplotlib import pyplot as plt
from collections import Counter
from serving_interface.srv import Order
import sqlite3
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

"""기본 설정"""
today_day = datetime.now().strftime("%y%m%d")
conn = None
cursor = None
today_count = None
robot_arrived = False
start_time = None
"""========"""

class KitchenDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.orders = []  # 주문 데이터 리스트
        self.completed_orders = []  # 출발된 메뉴 데이터
        self.total_price = 0  # 총 주문 가격
        self.init_ui()

        self.ros2_thread = threading.Thread(target=self.init_ros2_server, daemon=True)
        self.ros2_thread.start()

        self.popup_active = False

        self.check_timer = QTimer()
        self.check_timer.timeout.connect(self.check_robot_arrival)
        self.check_timer.start(100)

    def init_ros2_server(self):
        global conn, cursor, today_count
        conn = sqlite3.connect("ServingRobotDB.db",check_same_thread=False)
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM menu_order WHERE order_number LIKE '{today_day}%'"
        cursor.execute(query)
        today_count = cursor.fetchone()[0]

        rclpy.init()
        self.node = OrderServiceServer(self)
        rclpy.spin(self.node)
        rclpy.shutdown()

    def init_ui(self):
        self.setWindowTitle("주방 디스플레이")  # 디스플레이 제목
        self.setGeometry(100, 100, 1200, 700)  # 창 (x위치, y위치, 가로, 세로)

        # 메인 레이아웃
        self.main_layout = QVBoxLayout()

        # 상단 레이아웃 (테이블 별 주문 정보)
        self.table_layout = QHBoxLayout()
        self.table_widgets = []

        #왼쪽 세로칸 부터
        for _ in range(5):
            table_layout = QVBoxLayout()
            table_layout.setSpacing(15)

            # 테이블 번호
            table_label = QLabel("")
            table_label.setAlignment(Qt.AlignCenter)
            table_label.setStyleSheet("font-size: 20px; padding: 10px; background-color: #f0f0f0; "
                                       "border: 1px solid #ddd; font-weight: bold;")
            table_layout.addWidget(table_label)

            # 조리할 메뉴 목록
            pending_menu_list = QListWidget()
            pending_menu_list.setStyleSheet("font-size: 28px; background-color: #fff; border: 1px solid #ddd;")
            pending_menu_list.itemClicked.connect(lambda item, idx=len(self.table_widgets): self.move_to_completed(item, idx))  # 누르면 조리 완료 칸으로 가게끔
            table_layout.addWidget(pending_menu_list)

            # 완료된 메뉴 목록
            completed_menu_list = QListWidget()
            completed_menu_list.setStyleSheet("font-size: 28px; background-color: #f9f9f9; border: 1px solid #ddd;")
            table_layout.addWidget(completed_menu_list)

            # 로봇 출발 버튼
            start_button = QPushButton("출발")
            start_button.setEnabled(False)  # 초기에는 비활성화
            start_button.setStyleSheet("background-color: #FF5722; color: white; font-size: 18px; padding: 15px; "
                                        "border-radius: 5px;")
            start_button.clicked.connect(lambda _, idx=len(self.table_widgets): self.start_robot(idx))
            table_layout.addWidget(start_button)

            self.table_widgets.append((table_label, pending_menu_list, completed_menu_list, start_button))
            self.table_layout.addLayout(table_layout)

        # 정산 버튼
        self.settle_button = QPushButton("정산하기")
        self.settle_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 18px; padding: 15px; "
                                         "border-radius: 5px; margin: 10px;")
        self.settle_button.clicked.connect(self.show_settlement)

        # 추가 주문 영역
        self.extra_orders_label = QLabel("추가 주문")
        self.extra_orders_label.setStyleSheet("font-size: 20px; font-weight: bold; padding: 10px;")
        self.extra_orders_list = QListWidget()
        self.extra_orders_list.setStyleSheet("font-size: 18px; background-color: #fff; border: 1px solid #ddd;")

        self.extra_orders_layout = QVBoxLayout()
        self.extra_orders_layout.addWidget(self.extra_orders_label)
        self.extra_orders_layout.addWidget(self.extra_orders_list)

        self.table_layout.addLayout(self.extra_orders_layout)

        # 메인 레이아웃 구성
        self.main_layout.addLayout(self.table_layout)
        self.main_layout.addWidget(self.settle_button)
        self.setLayout(self.main_layout)

    # 정산 창 띄우는 메서드
    def show_settlement(self):
        settlement_window = SettlementWindow(self.orders, self.completed_orders, self.total_price)
        settlement_window.exec_()

    def check_robot_arrival(self):
        global robot_arrived

        if robot_arrived and not self.popup_active:

            self.popup_active = True
            self.show_popup("음식이 테이블에 도착했습니다!")

    def show_popup(self, message):
        popup = QDialog(self)
        popup.setWindowTitle("로봇 도착")
        popup.setWindowModality(Qt.ApplicationModal)
        popup.setGeometry(300, 300, 400, 200)

        label = QLabel(message, popup)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(50, 50, 300, 100)

        popup.show()

        QTimer.singleShot(3000, lambda: self.close_popup(popup))

    def close_popup(self, popup):
        global robot_arrived
        popup.close()
        robot_arrived = False
        self.popup_active = False


    # 새로운 주문 추가 : [[테이블번호, (메뉴1, 가격), (메뉴2, 가격)]] 형태
    def add_order(self, table_number, menu_price_pairs):
        """
        새로운 주문을 추가합니다. 메뉴는 (메뉴, 가격) 형태로 받습니다.
        """
        self.orders.append((table_number, menu_price_pairs))
        self.total_price += sum(price for _, price in menu_price_pairs)

        # if len(self.orders) <= 5:
        #     # 5개 이하일 때는 테이블 칸에 추가
        #     index = len(self.orders) - 1
        #     table_label, pending_menu_list, _, start_button = self.table_widgets[index]
        #     table_label.setText(f"테이블 {table_number}")
        #     for menu, price in menu_price_pairs:
        #         item = QListWidgetItem(f"{menu}")
        #         pending_menu_list.addItem(item)

        # else:
        #     # 5개 초과 주문은 추가 주문 리스트에 표시
        #     extra_order_text = f"테이블 {table_number} : " + ", ".join([f"{menu} " for menu, price in menu_price_pairs])
        #     self.extra_orders_list.addItem(extra_order_text)

        for table_label, pending_menu_list, _, start_button in self.table_widgets:
            if table_label.text() == "":
                table_label.setText(f"테이블 {table_number}")
                for menu, price in menu_price_pairs:
                    item = QListWidgetItem(f"{menu}")
                    pending_menu_list.addItem(item)
                return
        extra_order_text = f"테이블 {table_number} : " + ", ".join([f"{menu} " for menu, price in menu_price_pairs])
        self.extra_orders_list.addItem(extra_order_text)

    def move_to_completed(self, item, index):
        """
        클릭된 메뉴를 완료된 메뉴로 이동
        """
        _, pending_menu_list, completed_menu_list, start_button = self.table_widgets[index]
        completed_menu_list.addItem(item.text())  # 완료된 메뉴로 이동
        pending_menu_list.takeItem(pending_menu_list.row(item))  # 조리할 메뉴에서 삭제

        # 모든 메뉴가 완료된 경우 버튼 활성화 및 색깔 변경
        if pending_menu_list.count() == 0:
            start_button.setEnabled(True)
            start_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 15px; "
                                        "border-radius: 5px;")
        else:
            start_button.setEnabled(False)
            start_button.setStyleSheet("background-color: #FF5722; color: white; font-size: 18px; padding: 15px; "
                                        "border-radius: 5px;")

    def start_robot(self, index):
        """
        로봇 출발 처리
        """
        # 완료된 메뉴 초기화
        table_label, pending_menu_list, completed_menu_list, start_button = self.table_widgets[index]
        table_number = table_label.text().replace("테이블 ", "").strip()

        completed_menu_list.clear()
        table_label.setText("")
        pending_menu_list.clear()

        # 버튼 비활성화 및 색상 초기화
        start_button.setEnabled(False)
        start_button.setStyleSheet("background-color: #FF5722; color: white; font-size: 18px; padding: 15px; "
                                "border-radius: 5px;")

        # 기존 테이블 내용 왼쪽으로 Shift
        for i in range(index, len(self.table_widgets) - 1):
            next_label, next_pending, next_completed, next_button = self.table_widgets[i + 1]
            current_label, current_pending, current_completed, current_button = self.table_widgets[i]

            # 테이블 정보 이동
            current_label.setText(next_label.text())
            current_pending.clear()
            current_completed.clear()

            for j in range(next_pending.count()):
                current_pending.addItem(next_pending.item(j).text())
            for j in range(next_completed.count()):
                current_completed.addItem(next_completed.item(j).text())

            # 버튼 활성화 상태와 스타일 이동
            current_button.setEnabled(next_button.isEnabled())
            current_button.setStyleSheet(next_button.styleSheet())

            # 다음 테이블 데이터 초기화
            next_label.setText("")
            next_pending.clear()
            next_completed.clear()
            next_button.setEnabled(False)
            next_button.setStyleSheet("background-color: #FF5722; color: white; font-size: 18px; padding: 15px; "
                                    "border-radius: 5px;")

        # 추가 주문에서 첫 번째 주문을 맨 오른쪽으로 이동
        if self.extra_orders_list.count() > 0:
            next_order_text = self.extra_orders_list.takeItem(0).text()  # 첫 번째 추가 주문 텍스트를 가져옴
            last_label, last_pending, _, last_button = self.table_widgets[-1]  # 마지막 테이블 정보 가져옴
            
            # 테이블 번호와 메뉴 추출
            table_info, menu_info = next_order_text.split(":")  # 테이블 정보와 메뉴 정보를 분리
            table_label = table_info.strip()  # 테이블 번호
            last_label.setText(table_label)  # 마지막 테이블의 레이블에 테이블 번호 설정
            
            # 메뉴 항목을 나누어서 추가
            menu_items = menu_info.split(",")  # 메뉴 항목을 쉼표로 분리
            for menu_item in menu_items:
                menu_name = menu_item.split(" (")[0].strip()  # 메뉴 이름만 추출
                last_pending.addItem(menu_name)  # 메뉴 이름을 마지막 테이블의 '대기 메뉴' 목록에 추가
            
            # 추가된 마지막 테이블의 버튼 비활성화 및 색상 초기화
            last_button.setEnabled(False)
            last_button.setStyleSheet("background-color: #FF5722; color: white; font-size: 18px; padding: 15px; "
                                    "border-radius: 5px;")
        if table_number:
            self.node.send_goal(int(table_number))

class OrderServiceServer(Node):
    def __init__(self, display):
        super().__init__('order_service_server')
        self.display = display
        self.srv = self.create_service(Order, 'process_order', self.process_order_callback)
        self.action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def process_order_callback(self, request, response):
        self.get_logger().info(f"Received order: Table {request.table_num}, menu: {request.menu}, Total: {request.total_price}")

        menu_price_pairs = []
        menu_list = []
        for item in request.menu:
            menu, price = item.split(",")
            menu_price_pairs.append((menu.strip(), int(price.strip())))
            menu_list.append(menu)
        
        """주문 정보 삽입"""
        global today_count, today_day, cursor, conn
        menu_string = ",".join(menu_list)
        today_count +=1
        order_number = int(today_day+str(today_count))
        table_number = request.table_num
        order_time = datetime.now().strftime("%y%m%d %H%M%S")

        query = f"INSERT INTO menu_order VALUES ({order_number},'{order_time}','{menu_string}',{table_number})"
        cursor.execute(query)
        conn.commit()
        self.get_logger().info("order info insert")
        """=============="""

        self.display.add_order(request.table_num, menu_price_pairs)

        response.is_accept = True
        return response

    def send_goal(self, table_number):
        self.action_client.wait_for_server()
        self.get_logger().info(f"Sending TurtleBot to table {table_number}")
        
        global start_time
        start_time = str(datetime.now().strftime())

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = self.get_table_pose(table_number)
        future = self.action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        future.add_done_callback(self.goal_response_callback)

    def get_table_pose(self, table_number):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = self.get_clock().now().to_msg()

        table_positions = {
            1: (1.28, 1.60, 0.99, 0.02),
            2: (1.30, 0.49, -0.99, 0.02),
            3: (1.31, -0.49, -0.66, 0.74),
            4: (2.48, 1.65, -0.99, 0.11),
            5: (2.46, 0.51, -0.99, 0.02),
            6: (2.41, -0.62, -0.99, 0.01),
            7: (3.65, 1.61, -0.99, 0.06),
            8: (3.91, 0.51, 0.99, 0.02),
            9: (3.76, -0.67, -0.99, 0.0)
        }

        x, y, z, w = table_positions.get(table_number, (0.0, 0.0, 0.0, 1.0))
        pose.pose.position.x = x
        pose.pose.position.y = y
        pose.pose.orientation.z = z
        pose.pose.orientation.w = w

        return pose

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f"Remaining distance: {feedback.distance_remaining:.2f}m")

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected")
            return

        self.get_logger().info("Goal accepted")
        goal_handle.get_result_async().add_done_callback(self.result_callback)

    def result_callback(self, future):
        self.get_logger().info("Goal result: TurtleBot has reached the table.")

        global robot_arrived, start_time, cursor, conn
        robot_arrived = True

        end_time = str(datetime.now())
        query = f"INSERT INTO moving VALUES ('{start_time}','{end_time}')"
        cursor.execute(query)
        conn.commit()


class SettlementWindow(QDialog):
    def __init__(self, orders, completed_orders, total_price):
        super().__init__()
        self.setWindowTitle("정산 내역")
        self.setGeometry(200, 200, 400, 900)

        # 기존 정산 테이블 생성
        table_widget = QTableWidget(self)
        table_widget.setRowCount(sum(len(menu_price_pairs) for _, menu_price_pairs in orders + completed_orders))  # 모든 메뉴 수로 행 수 설정
        table_widget.setColumnCount(3)
        table_widget.setHorizontalHeaderLabels(["테이블", "메뉴", "가격"])

        row = 0
        for table_number, menu_price_pairs in orders + completed_orders:
            for menu, price in menu_price_pairs:
                table_widget.setItem(row, 0, QTableWidgetItem(str(table_number)))
                table_widget.setItem(row, 1, QTableWidgetItem(menu))
                table_widget.setItem(row, 2, QTableWidgetItem(str(price)))
                row += 1

        total_label = QLabel(f"총액: {total_price} 원", self)

        # 그래프 보기 버튼 추가
        self.graph_button = QPushButton("그래프 보기", self)
        self.graph_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; "
                                        "border-radius: 5px;")
        self.graph_button.clicked.connect(self.show_graph)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(table_widget)
        layout.addWidget(total_label)
        layout.addWidget(self.graph_button)  # 그래프 버튼 추가

        self.setLayout(layout)
        self.orders = orders + completed_orders  # 주문 데이터 저장

    def show_graph(self):
        """
        메뉴별 판매 건수를 그래프로 표시합니다.
        """
        # 한글 깨짐 방지
        #plt.rcParams["font.family"] = 'NanumGothic'
        #mpl.rcParams['axes.unicode_minus'] = False  # 마이너스 폰트 깨짐 방지
        mpl.use('Qt5Agg')

        total_prices_day, today_dates = self.cal_per_day()
        total_prices_mon, today_months = self.cal_per_month()

        plt.figure(figsize=(10,6))
        plt.subplot(1,2,1)
        plt.plot(today_dates, total_prices_day)
        plt.title("sales per day")
        plt.xlabel("days")
        plt.ylabel("sales(won)")
        plt.subplot(1,2,2)
        plt.plot(today_months, total_prices_mon)
        plt.title("sales per month")
        plt.xlabel("months")
        plt.tight_layout()
        plt.show()


        # # 메뉴별 판매 건수 계산
        # menu_counts = Counter(menu for _, menu_price_pairs in self.orders for menu, _ in menu_price_pairs)


        # # 그래프 생성
        # plt.figure(figsize=(10, 6))
        # plt.bar(menu_counts.keys(), menu_counts.values(), color='skyblue')
        # plt.title("메뉴별 판매 건수", fontsize=16)
        # plt.xlabel("메뉴", fontsize=12, )
        # plt.ylabel("판매 건수", fontsize=12)
        # plt.xticks(rotation=45, ha="right")
        # plt.yticks(range(0, max(menu_counts.values()) + 1))  # 정수로 눈금 설정
        # plt.tight_layout()
        # plt.show()

    def cal_per_day(self):
        
        global cursor

        total_prices = []
        today_dates = []

        for i in range(5):
            today = (datetime.now() + timedelta(days=-i)).strftime("%y%m%d")
            qeury = f"SELECT * FROM menu_order WHERE order_number LIKE '{today}%'"
            cursor.execute(qeury)
            orders = cursor.fetchall()
            today_dates.append(today)
            if len(orders) == 0 :
                total_prices.append(0)
            else:
                sum = 0
                for order in orders:
                    menu_list = order[2]
                    menu_list = menu_list.split(',')

                    for menu in menu_list:
                        qeury = f"SELECT price FROM menu WHERE name='{menu}'"
                        cursor.execute(qeury)
                        price = cursor.fetchone()[0]
                        sum += price
                total_prices.append(sum)
        
        total_prices.reverse()
        today_dates.reverse()

        return total_prices, today_dates

    def cal_per_month(self):
        
        global cursor

        total_prices = []
        today_months = []

        for i in range(5):
            today = (datetime.now() - relativedelta(months=i)).strftime("%y%m")
            qeury = f"SELECT * FROM menu_order WHERE order_number LIKE '{today}%'"
            cursor.execute(qeury)
            orders = cursor.fetchall()
            today_months.append(today)
            if len(orders) == 0 :
                total_prices.append(0)
            else:
                sum = 0
                for order in orders:
                    menu_list = order[2]
                    menu_list = menu_list.split(',')

                    for menu in menu_list:
                        qeury = f"SELECT price FROM menu WHERE name='{menu}'"
                        cursor.execute(qeury)
                        price = cursor.fetchone()[0]
                        sum += price
                total_prices.append(sum)
        
        total_prices.reverse()
        today_months.reverse()

        return total_prices, today_months


def main(args=None):
    global conn
    app = QApplication(sys.argv)
    kitchen_display = KitchenDisplay()
    kitchen_display.show()
    sys.exit(app.exec_())
    conn.close()


if __name__ == '__main__':
    main()

    # kitchen_display.add_order(1, [("김치찌개", 7000), ("된장찌개", 6000)])
    # kitchen_display.add_order(5, [("해물탕", 25000)])
    # kitchen_display.add_order(8, [("계란말이", 8000), ("라면", 3000), ("무구리", 35000)])
    # kitchen_display.add_order(9, [("소주", 4000), ("콜라", 2000)])
    # kitchen_display.add_order(4, [("짜파구리", 9000)])
    # kitchen_display.add_order(2, [("양파", 1000), ("공기밥", 1000)])
    # kitchen_display.add_order(3, [("먹태", 6000), ("짜파구리", 9000), ("오뎅탕", 15000), ("된장찌개", 6000)])
    # kitchen_display.add_order(7, [("과자 리필", 0), ("소주", 4000), ("맥주", 4000), ("파인샤베트", 5000), ("된장찌개", 6000), ("콜라", 2000)])
    # kitchen_display.add_order(5, [("계란말이", 8000), ("라면", 3000), ("무구리", 35000)])


    

