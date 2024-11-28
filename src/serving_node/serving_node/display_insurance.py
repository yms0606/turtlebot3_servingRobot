from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem, QDialog
from PyQt5.QtCore import Qt
import sys

class KitchenDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.orders = []  # 주문 데이터 리스트
        self.completed_orders = []  # 출발된 메뉴 데이터
        self.total_price = 0  # 총 주문 가격
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("주방 디스플레이")
        self.setGeometry(100, 100, 1200, 700)  # 창 크기 확대

        # 메인 레이아웃
        self.main_layout = QVBoxLayout()

        # 상단 레이아웃 (테이블 별 주문 정보)
        self.table_layout = QHBoxLayout()
        self.table_widgets = []

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
            pending_menu_list.itemClicked.connect(lambda item, idx=len(self.table_widgets): self.move_to_completed(item, idx))
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

    def add_order(self, table_number, menu_price_pairs):
        """
        새로운 주문을 추가합니다. 메뉴는 (메뉴, 가격) 형태로 받습니다.
        """
        self.orders.append((table_number, menu_price_pairs))
        self.total_price += sum(price for _, price in menu_price_pairs)

        if len(self.orders) <= 5:
            # 5개 이하일 때는 테이블 칸에 추가
            index = len(self.orders) - 1
            table_label, pending_menu_list, _, start_button = self.table_widgets[index]
            table_label.setText(f"테이블 {table_number}")
            for menu, price in menu_price_pairs:
                item = QListWidgetItem(f"{menu}")
                pending_menu_list.addItem(item)

        else:
            # 5개 초과 주문은 추가 주문 리스트에 표시
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
        completed_menu_list.clear()
        table_label.setText("")
        pending_menu_list.clear()

        # 버튼 비활성화 및 색상 초기화
        start_button.setEnabled(False)
        start_button.setStyleSheet("background-color: #FF5722; color: white; font-size: 18px; padding: 15px; "
                                "border-radius: 5px;")

        # 기존 테이블 내용 왼쪽으로 Shift
        for i in range(index, 4):
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
            last_label, last_pending, _, last_button = self.table_widgets[4]  # 마지막 테이블 정보 가져옴
            
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



    def show_settlement(self):
        """
        정산하기 버튼을 눌렀을 때 호출
        """
        settlement_window = SettlementWindow(self.orders, self.completed_orders, self.total_price)
        settlement_window.exec_()


class SettlementWindow(QDialog):
    def __init__(self, orders, completed_orders, total_price):
        super().__init__()
        self.setWindowTitle("정산 내역")
        self.setGeometry(200, 200, 1200, 900)

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
        layout = QVBoxLayout()
        layout.addWidget(table_widget)
        layout.addWidget(total_label)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    kitchen_display = KitchenDisplay()
    kitchen_display.show()

    kitchen_display.add_order(1, [("김치찌개", 7000), ("된장찌개", 6000)])
    kitchen_display.add_order(5, [("해물탕", 25000)])
    kitchen_display.add_order(8, [("계란말이", 8000), ("라면", 3000), ("무구리", 35000)])
    kitchen_display.add_order(9, [("소주", 4000), ("콜라", 2000)])
    kitchen_display.add_order(4, [("짜파구리", 9000)])

    
    kitchen_display.add_order(2, [("양파", 1000), ("공기밥", 1000)])
    kitchen_display.add_order(3, [("먹태", 6000), ("짜파구리", 9000), ("오뎅탕", 15000)])
    kitchen_display.add_order(7, [("과자 리필", 0), ("소주", 4000), ("맥주", 4000), ("파인샤베트", 5000), ("된장찌개", 6000), ("콜라", 2000)])
    kitchen_display.add_order(5, [("계란말이", 8000), ("라면", 3000), ("무구리", 35000)])


    sys.exit(app.exec_())
