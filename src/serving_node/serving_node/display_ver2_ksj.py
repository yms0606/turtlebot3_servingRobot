from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
import sys


class KitchenDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.orders = [None] * 6  # 최대 6개의 테이블 정보 저장 (각 테이블은 메뉴 리스트)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("주방 디스플레이")
        self.setGeometry(100, 100, 800, 600)

        # 메인 레이아웃
        self.main_layout = QVBoxLayout()

        # 테이블 영역 레이아웃
        self.table_layout = QHBoxLayout()
        self.table_widgets = []  # 테이블 위젯들을 저장할 리스트
        for i in range(6):
            table_widget = self.create_table_widget(i + 1)  # 테이블 위젯 생성
            self.table_widgets.append(table_widget)
            self.table_layout.addLayout(table_widget)

        # 메인 레이아웃에 테이블 레이아웃 추가
        self.main_layout.addLayout(self.table_layout)

        # 정산 버튼 추가
        self.settle_button = QPushButton("정산하기")
        self.settle_button.clicked.connect(self.reset_orders)
        self.settle_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 14px; padding: 10px; "
                                         "border-radius: 5px; margin: 10px;")
        self.main_layout.addWidget(self.settle_button)

        self.setLayout(self.main_layout)

    def create_table_widget(self, table_number):
        """
        각 테이블의 위젯(레이아웃)을 생성합니다.
        """
        layout = QVBoxLayout()

        # 테이블 이름 표시
        table_label = QLabel(f"테이블 {table_number}")
        table_label.setAlignment(Qt.AlignCenter)
        table_label.setStyleSheet("font-size: 16px; color: #333; padding: 10px; background-color: #f9f9f9; "
                                  "border: 1px solid #ddd; border-radius: 5px; font-weight: bold;")
        layout.addWidget(table_label)

        # 메뉴 레이블 추가 (최대 3개)
        menu_labels = []
        for _ in range(3):
            menu_label = QLabel("대기 중")
            menu_label.setAlignment(Qt.AlignCenter)
            menu_label.setStyleSheet("font-size: 14px; color: #666; padding: 8px; background-color: #fff; "
                                     "border: 1px solid #ddd; border-radius: 5px;")
            # 메뉴 클릭 시 완료 처리
            menu_label.mousePressEvent = lambda event, label=menu_label: self.complete_menu(label)
            menu_labels.append(menu_label)
            layout.addWidget(menu_label)

        # 출발 버튼
        start_button = QPushButton("출발")
        start_button.setEnabled(False)
        start_button.clicked.connect(lambda: self.start_order(table_number - 1))
        start_button.setStyleSheet("background-color: #FF5722; color: white; font-size: 14px; padding: 10px; "
                                   "border-radius: 5px; margin: 5px;")
        layout.addWidget(start_button)

        # 테이블 관련 정보 저장
        layout.menu_labels = menu_labels
        layout.start_button = start_button
        return layout

    def add_order(self, table_number, menus):
        """
        주문을 추가합니다.
        """
        # 새로운 주문이 들어오면 가장 오래된 주문을 제거
        if None not in self.orders and len(self.orders) == 6:
            self.orders.pop(0)
            self.orders.append(None)

        # 해당 테이블에 주문 추가
        self.orders[table_number - 1] = menus
        self.update_table(table_number - 1)

    def update_table(self, table_index):
        """
        테이블의 UI를 주문 정보로 업데이트합니다.
        """
        order = self.orders[table_index]
        table_widget = self.table_widgets[table_index]
        if order is not None:
            for i, menu_label in enumerate(table_widget.menu_labels):
                if i < len(order):
                    menu_label.setText(order[i])
                    menu_label.setStyleSheet("font-size: 14px; color: #666; padding: 8px; background-color: #fff; "
                                             "border: 1px solid #ddd; border-radius: 5px;")
                else:
                    menu_label.setText("대기 중")
            table_widget.start_button.setEnabled(False)
        else:
            for menu_label in table_widget.menu_labels:
                menu_label.setText("대기 중")
            table_widget.start_button.setEnabled(False)

    def complete_menu(self, label):
        """
        메뉴를 클릭하여 완료 처리합니다.
        """
        if label.text() == "대기 중" or label.text() == "완료":
            return
        label.setText("완료")
        label.setStyleSheet("font-size: 14px; color: green; padding: 8px; background-color: #e8f5e9; "
                            "border: 1px solid #a5d6a7; border-radius: 5px;")

        # 모든 메뉴가 완료되었는지 확인
        for table_widget in self.table_widgets:
            if all(menu_label.text() == "완료" for menu_label in table_widget.menu_labels):
                table_widget.start_button.setEnabled(True)

    def start_order(self, table_index):
        """
        출발 버튼을 클릭했을 때 처리.
        """
        self.orders[table_index] = None
        self.update_table(table_index)

    def reset_orders(self):
        """
        정산 버튼 클릭 시 모든 주문 초기화.
        """
        self.orders = [None] * 6
        for i in range(6):
            self.update_table(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kitchen_display = KitchenDisplay()
    kitchen_display.show()

    # 테스트용 주문 추가
    kitchen_display.add_order(1, ["김치찌개", "된장찌개"])
    kitchen_display.add_order(2, ["비빔밥"])
    kitchen_display.add_order(3, ["불고기", "라면"])
    kitchen_display.add_order(4, ["김밥", "떡볶이", "순대"])
    kitchen_display.add_order(5, ["스파게티", "피자"])
    kitchen_display.add_order(6, ["햄버거", "감자튀김", "치킨"])

    sys.exit(app.exec_())
