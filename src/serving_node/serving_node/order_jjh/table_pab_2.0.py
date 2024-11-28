import sys
import os
import sqlite3
import io
from PIL import ImageQt
import rclpy
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QByteArray, QBuffer
from rclpy.node import Node
from serving_interface.srv import Order
from serving_interface.srv import ServingStatus

class ROS2OrderClient(Node):
    def __init__(self):
        super().__init__('ros2_order_client')
        self.client = self.create_client(Order, 'process_order')
        while not self.client.wait_for_service(timeout_sec = 1.0):
            self.get_logger().info('Waiting for order...')

    def send_order(self, table_num, menu, total_price):
        request = Order.Request()
        request.table_num = table_num
        request.menu = menu
        request.total_price = total_price

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result():
            response = future.result()
            return response.is_accept
        else:
            self.get_logger().error('Service call failed')
            return False
        
class ServingStatusServer(Node):
    def __init__(self):
        super().__init__('serving_status_server')
        self.srv = self.create_service(ServingStatus, 'serving_status', self.handle_serving_status)

    def handle_serving_status(self, request, response):
        if request.is_arrived:
            self.get_logger().info('TurtleBot has arrived at the table.')
            self.show_arrival_popup()
            response.get_back = self.handle_return_request()
        else:
            self.get_logger().info('TurtleBot did not arrive.')
            response.get_back = False
        return response

    def show_arrival_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("TurtleBot Status")
        msg.setText("TurtleBot has arrived at the table!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def handle_return_request(self):
        msg = QMessageBox()
        msg.setWindowTitle("Return Request")
        msg.setText("Do you want the TurtleBot to return?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg.exec_()
        return result == QMessageBox.Yes

class TableOrderApp(QMainWindow):
    def __init__(self, menu_files):
        super().__init__()
        self.setWindowTitle("부리부리대마왕포차")
        self.setGeometry(100, 100, 1200, 800)

        self.ros2_thread = threading.Thread(target=self.init_ros2_client, daemon=True)
        self.ros2_thread.start()

        # 메뉴 데이터 로드
        self.menu_data = self.load_menu_data(menu_files)
        self.current_category = None

        # 장바구니 데이터
        self.cart = {}

        # 메인 위젯
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # 상단 - 테이블 번호
        top_layout = QHBoxLayout()
        table_label = QLabel("NO.3")
        table_label.setStyleSheet("font-size: 30px; font-weight: bold; padding: 10px;")
        table_label.setAlignment(Qt.AlignLeft)
        top_layout.addWidget(table_label)

        top_placeholder = QLabel("")  # 중앙 정렬 유지용
        top_layout.addWidget(top_placeholder)

        top_widget = QWidget()
        top_widget.setLayout(top_layout)
        main_layout.addWidget(top_widget)

        # 중앙 화면 - 좌/우 레이아웃
        center_layout = QHBoxLayout()

        # 왼쪽 영역 - 카테고리
        self.category_list = QVBoxLayout()
        category_widget = QWidget()
        category_widget.setLayout(self.category_list)
        category_scroll = QScrollArea()
        category_scroll.setWidget(category_widget)
        category_scroll.setWidgetResizable(True)
        category_scroll.setFixedWidth(200)
        category_scroll.setStyleSheet("background-color: #f4f4f4; border: none;")

        # 카테고리 버튼 추가
        for category in self.menu_data.keys():
            button = QPushButton(category)
            button.setStyleSheet("""
                font-size: 18px; 
                padding: 15px; 
                margin: 5px 0; 
                border: 2px solid #ccc; 
                background-color: #ffffff; 
                border-radius: 10px;
                text-align: center;
            """)
            button.clicked.connect(lambda _, cat=category: self.scroll_to_category(cat))
            self.category_list.addWidget(button)

        # 직원 호출 버튼 추가
        call_staff_button = QPushButton("직원 호출")
        call_staff_button.setStyleSheet("""
            font-size: 18px; 
            padding: 10px; 
            margin: 20px 0; 
            background-color: #FF5733; 
            color: white; 
            border-radius: 10px;
        """)
        call_staff_button.clicked.connect(self.call_staff)  # 클릭 이벤트 연결
        self.category_list.addWidget(call_staff_button)

        # 중앙 - 메뉴
        self.menu_layout = QVBoxLayout()
        menu_widget = QWidget()
        menu_widget.setLayout(self.menu_layout)
        self.menu_scroll = QScrollArea()  # menu_scroll을 클래스 변수로 저장
        self.menu_scroll.setWidget(menu_widget)
        self.menu_scroll.setWidgetResizable(True)
        self.menu_scroll.setStyleSheet("border-right: 2px solid #ccc;")

        # 모든 카테고리와 메뉴 표시
        self.show_all_categories()

        # 오른쪽 - 장바구니
        right_layout = QVBoxLayout()
        right_frame = QWidget()
        right_frame.setLayout(right_layout)
        right_frame.setFixedWidth(302)

        # 장바구니 테이블
        self.cart_table = QTableWidget()
        self.cart_table.setColumnCount(3)  # 4 -> 3으로 변경하여 불필요한 열 제거
        self.cart_table.setHorizontalHeaderLabels(["메뉴", "수량", "현재 가격"])
        self.cart_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.cart_table.setStyleSheet("font-size: 14px;")
        self.cart_table.setFixedHeight(500)  # 장바구니 테이블 높이 고정
        right_layout.addWidget(self.cart_table)

        # 열 폭 조정
        self.cart_table.setColumnWidth(0, 90)  # 메뉴
        self.cart_table.setColumnWidth(1, 100)   # 수량
        self.cart_table.setColumnWidth(2, 80)   # 현재 가격

        # 총 금액 및 버튼
        self.total_label = QLabel("총 금액: 0원")
        self.total_label.setAlignment(Qt.AlignRight)
        self.total_label.setStyleSheet("font-size: 20px; padding: 10px; color: red;")
        right_layout.addWidget(self.total_label)

        clear_cart_button = QPushButton("전체 제거")
        clear_cart_button.setStyleSheet("font-size: 16px; padding: 10px; background-color: #FF4D4D; color: white;")
        clear_cart_button.clicked.connect(self.clear_cart)
        right_layout.addWidget(clear_cart_button)

        order_button = QPushButton("주문하기")
        order_button.setStyleSheet("font-size: 18px; padding: 10px; background-color: #4CAF50; color: white;")
        right_layout.addWidget(order_button)

        # 레이아웃 배치
        center_layout.addWidget(category_scroll)  # 왼쪽 카테고리
        center_layout.addWidget(self.menu_scroll)  # 중앙 메뉴
        center_layout.addWidget(right_frame)  # 오른쪽 장바구니

        main_layout.addLayout(center_layout)


        order_button.clicked.connect(self.show_payment_popup)  # 결제 팝업
        
    def scroll_to_category(self, category):
        """카테고리 버튼 클릭 시 해당 위치로 스크롤"""
        if category in self.category_positions:
            target_widget = self.category_positions[category]
            # QScrollArea의 verticalScrollBar를 사용하여 스크롤 이동
            self.menu_scroll.verticalScrollBar().setValue(target_widget.y())

    def call_staff(self):
        """직원 호출 버튼 클릭 시 팝업 표시"""
        message_box = QMessageBox()
        message_box.setWindowTitle("직원 호출")
        message_box.setText("직원이 호출되었습니다!")
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def init_ros2_client(self):
        rclpy.init()
        self.ros2_client = ROS2OrderClient()

    def load_menu_data(self, menu_files):
        """메뉴 파일에서 카테고리와 메뉴 데이터를 로드"""
        menu_data = {}
        menu_data['메인메뉴'] = []
        menu_data['사이드메뉴'] = []
        menu_data['음료'] = []
        menu_data['주류'] = []
        # for file in menu_files:
        #     category = os.path.splitext(os.path.basename(file))[0]  # 파일 이름을 카테고리로
        #     menu_data[category] = []
        #     with open(file, 'r', encoding='utf-8') as f:
        #         for line in f:
        #             line = line.strip()  # 양쪽 공백 제거
        #             if not line:  # 빈 줄 무시
        #                 continue
        #             try:
        #                 name, price = line.split(" - ")
        #                 menu_data[category].append((name, int(price)))
        #             except ValueError:
        #                 print(f"잘못된 데이터 무시: {line}")
        #                 continue
        
        conn = sqlite3.connect("/home/kim/Desktop/drive1_ws/turtlebot3_servingRobot/ServingRobotDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM menu")
        datas = cursor.fetchall()

        for data in datas:
            menu_data[data[1]].append((data[0],int(data[2])))

        cursor.close()

        return menu_data

    def show_all_categories(self):
        """모든 카테고리와 메뉴를 한꺼번에 표시"""
        # 기존 메뉴 초기화
        for i in reversed(range(self.menu_layout.count())):
            self.menu_layout.itemAt(i).widget().deleteLater()

        # 카테고리별 메뉴 추가
        self.category_positions = {}  # 카테고리 위치 저장
        for category, items in self.menu_data.items():
            # 카테고리 라벨 추가
            category_label = QLabel(category)
            category_label.setAlignment(Qt.AlignCenter)
            category_label.setStyleSheet("""
                font-size: 30px; 
                font-weight: bold; 
                margin: 10px; 
                
            """)
            self.menu_layout.addWidget(category_label)

            # 카테고리 위치 저장
            self.category_positions[category] = category_label

            # 메뉴 카드 추가

            conn = sqlite3.connect("/home/kim/Desktop/drive1_ws/turtlebot3_servingRobot/ServingRobotDB.db")
            cursor = conn.cursor()

            item_grid = QGridLayout()
            for index, (menu_name, price) in enumerate(items):
                # 메뉴 카드
                card = QWidget()
                card.setStyleSheet("""
                    background-color: #ffffff;
                    border: 2px solid #ccc;
                    border-radius: 10px;
                    padding: 10px;
                    width: 180px;
                    margin: 5px;
                """)
                card_layout = QVBoxLayout(card)

                query = f"SELECT img FROM image_file WHERE name='{menu_name}'"
                cursor.execute(query)
                img = cursor.fetchone()
                img = img[0]

                byte_array = QByteArray(img)
                buffer = QBuffer(byte_array)
                buffer.open(QBuffer.ReadOnly)
                
                pixmap = QPixmap()
                pixmap.loadFromData(buffer.data())
                pixmap = pixmap.scaled(160,100, Qt.KeepAspectRatio)
                
                # 이미지
                image_label = QLabel()
                # image_path = f"./images/{menu_name}.png"
                # if os.path.exists(image_path):
                #     pixmap = QPixmap(image_path).scaled(160, 100, Qt.KeepAspectRatio)
                # else:
                #     pixmap = QPixmap(160, 100)
                #     pixmap.fill(Qt.lightGray)
                image_label.setPixmap(pixmap)
                image_label.setAlignment(Qt.AlignCenter)

                # 메뉴 이름과 가격
                name_label = QLabel(menu_name)
                name_label.setAlignment(Qt.AlignCenter)
                name_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 5px;")

                price_label = QLabel(f"{price:,}원")  # 천 단위 구분 추가
                price_label.setAlignment(Qt.AlignCenter)
                price_label.setStyleSheet("font-size: 15px; color: #333; margin-bottom: 10px;")

                # 카드 구성
                card_layout.addWidget(image_label)
                card_layout.addWidget(name_label)
                card_layout.addWidget(price_label)

                # 카드 클릭 이벤트
                card.mousePressEvent = lambda _, n=menu_name, p=price: self.add_to_cart(n, p)

                # 카드 추가
                row, col = divmod(index, 3)
                item_grid.addWidget(card, row, col)

            self.menu_layout.addLayout(item_grid)

    def add_to_cart(self, name, price):
        """메뉴를 장바구니에 추가"""
        if name in self.cart:
            self.cart[name]['quantity'] += 1
        else:
            self.cart[name] = {'price': price, 'quantity': 1}
        self.update_cart()

    def update_cart(self):
        """장바구니 테이블 업데이트"""
        self.cart_table.setRowCount(len(self.cart))
        total = 0
        for row, (name, data) in enumerate(self.cart.items()):
            total += data['price'] * data['quantity']

            # 메뉴 이름
            self.cart_table.setItem(row, 0, QTableWidgetItem(name))

            # 수량 조작 레이아웃 (수량 표시 + 증가/감소 버튼)
            quantity_widget = QWidget()
            quantity_layout = QHBoxLayout(quantity_widget)
            quantity_layout.setContentsMargins(0, 0, 0, 0)

            # 감소 버튼
            decrease_button = QPushButton("-")
            decrease_button.setFixedSize(30, 30)
            decrease_button.setStyleSheet("font-size: 14px;")
            decrease_button.clicked.connect(lambda _, n=name: self.decrease_quantity(n))
            quantity_layout.addWidget(decrease_button)

            # 수량 표시
            quantity_label = QLabel(str(data['quantity']))
            quantity_label.setAlignment(Qt.AlignCenter)
            quantity_layout.addWidget(quantity_label)

            # 증가 버튼
            increase_button = QPushButton("+")
            increase_button.setFixedSize(30, 30)
            increase_button.setStyleSheet("font-size: 14px;")
            increase_button.clicked.connect(lambda _, n=name: self.increase_quantity(n))
            quantity_layout.addWidget(increase_button)

            self.cart_table.setCellWidget(row, 1, quantity_widget)

            # 현재 가격
            self.cart_table.setItem(row, 2, QTableWidgetItem(f"{data['price'] * data['quantity']:,}원"))

        self.total_label.setText(f"총 금액: {total:,}원")
        

    def increase_quantity(self, name):
        """수량 증가"""
        if name in self.cart:
            self.cart[name]['quantity'] += 1
        self.update_cart()

    def decrease_quantity(self, name):
        """수량 감소"""
        if name in self.cart and self.cart[name]['quantity'] > 0:
            self.cart[name]['quantity'] -= 1
        if self.cart[name]['quantity'] == 0:
            self.cart.pop(name)
        self.update_cart()


    def clear_cart(self):
        """장바구니 전체 제거"""
        self.cart.clear()
        self.update_cart()



    def show_payment_popup(self):
        """결제 확인 팝업 표시"""
        popup = QDialog(self)
        popup.setWindowTitle("결제 확인")
        popup.setGeometry(400, 300, 300, 200)

        popup_layout = QVBoxLayout()
        popup.setLayout(popup_layout)

        # 팝업 제목
        title = QLabel("장바구니의 상품과 수량을 확인하셨습니까?")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 14px; font-weight: bold; color: red;")
        popup_layout.addWidget(title)

        # 장바구니 내용 표시
        for name, details in self.cart.items():
            item_label = QLabel(f"{name}: {details['quantity']}개 - {details['price'] * details['quantity']:,}원")
            item_label.setStyleSheet("font-size: 15px;")
            popup_layout.addWidget(item_label)

        # 총 금액 표시
        total_price = sum(item['price'] * item['quantity'] for item in self.cart.values())
        total_label = QLabel(f"합계: {total_price:,}원")
        total_label.setAlignment(Qt.AlignRight)
        total_label.setStyleSheet("font-size: 15px; color: red;")
        popup_layout.addWidget(total_label)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()

        cancel_button = QPushButton("취소")
        cancel_button.setStyleSheet("font-size: 15px;")
        cancel_button.clicked.connect(popup.close)
        button_layout.addWidget(cancel_button)

        pay_button = QPushButton("결제하기")
        pay_button.setStyleSheet("font-size: 15px; background-color: red; color: white;")
        pay_button.clicked.connect(self.process_payment)
        pay_button.clicked.connect(popup.close)
        button_layout.addWidget(pay_button)

        popup_layout.addLayout(button_layout)

        popup.exec_()

    def process_payment(self, popup):
        table_num = 3
        menu = [f"{name} x {details['quantity']}" for name, details in self.cart.items()]
        total_price = sum(item['price'] * item['quantity'] for item in self.cart.values())

        def send_request():
            is_accept = self.ros2_client.send_order(table_num, menu, total_price)
            if is_accept:
                QMessageBox.information(self, "결제 완료", "주문이 접수되었습니다!")
                self.cart.clear()
                self.update_cart()
            else:
                QMessageBox.warning(self, "결제 실패", "주문에 실패했습니다.")
        
        threading.Thread(target=send_request, daemon=True).start()
        popup.close()


if __name__ == "__main__":
    menu_files = ["메인 메뉴.txt", "사이드 메뉴.txt", "주류.txt","음료.txt"]
    app = QApplication(sys.argv)
    window = TableOrderApp(menu_files)
    window.show()
    sys.exit(app.exec_())
