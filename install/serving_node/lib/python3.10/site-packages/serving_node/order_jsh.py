import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QGridLayout, QFrame, QWidget, QScrollArea, QSpacerItem, QSizePolicy, QDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Application")
        self.setGeometry(100, 100, 1280, 720)
        self.cart_items = {}  # 장바구니 항목 저장
        self.cart_total = 0
        self.category_positions = {}  # 카테고리 위치 저장
        # 메뉴 데이터 (이름과 가격)
        self.menu_data = [
            {"name": "김치찌개", "price": 9000},
            {"name": "된장찌개", "price": 8500},
            {"name": "불고기", "price": 12000},
            {"name": "비빔밥", "price": 8000},
            {"name": "육개장", "price": 9500},
            {"name": "칼국수", "price": 7500},
            {"name": "냉면", "price": 8500},
            {"name": "삼겹살", "price": 14000},
            {"name": "소고기구이", "price": 20000},
            {"name": "제육볶음", "price": 9500},
            {"name": "치킨", "price": 15000},
            {"name": "떡볶이", "price": 7000},
            {"name": "순대국", "price": 8000},
            {"name": "회덮밥", "price": 13000},
            {"name": "우동", "price": 7500},
            {"name": "오징어볶음", "price": 10000},
            {"name": "잡채", "price": 11000},
            {"name": "파전", "price": 12000},
            {"name": "해물탕", "price": 25000},
            {"name": "막국수", "price": 8500},
        ]
        self.setup_ui()

    def setup_ui(self):
        # 메인 컨테이너
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # 왼쪽: 카테고리
        category_layout = QVBoxLayout()

        # 카테고리 버튼 생성
        categories = {"전골류": 3, "포장": 4, "사이드": 5, "음료": 4, "주류": 4, "추가반찬": 4}
        self.categories = categories
        self.category_buttons = {}

        for cat in categories.keys():
            button_layout = QVBoxLayout()  # 개별 버튼 레이아웃
            button = QPushButton(cat)
            button.setFixedHeight(50)
            button.setFixedWidth(150)
            button.setFont(QFont("Arial", 12))
            button.setStyleSheet("""
                QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #cccccc;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #e6e6e6;
                }
            """)
            button.clicked.connect(lambda _, c=cat: self.scroll_to_category(c))
            self.category_buttons[cat] = button

            # 버튼 추가
            button_layout.addWidget(button)

            # 버튼 간격 설정 (레이아웃 간 간격을 줄임)
            button_layout.setContentsMargins(0, 0, 0, 0)  # 위/아래 간격 3픽셀로 설정
            button_layout.setSpacing(3)

            category_layout.addLayout(button_layout)

        # 직원 호출 버튼 추가
        staff_call_button = QPushButton("직원 호출")
        staff_call_button.setFixedHeight(50)
        staff_call_button.setFixedWidth(150)
        staff_call_button.setFont(QFont("Arial", 12))
        staff_call_button.setStyleSheet("""
            QPushButton {
                background-color: #ff4d4d;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #ff6666;
            }
        """)
        staff_call_button.clicked.connect(self.show_staff_call_popup)
        category_layout.addWidget(staff_call_button)

        # 왼쪽 레이아웃 추가
        main_layout.addLayout(category_layout)

        # 중간: 메뉴 스크롤 영역
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.menu_frame = QWidget()
        self.menu_layout = QVBoxLayout()
        self.menu_frame.setLayout(self.menu_layout)
        self.scroll_area.setWidget(self.menu_frame)
        main_layout.addWidget(self.scroll_area, stretch=3)

        # 오른쪽: 장바구니
        cart_layout = QVBoxLayout()

        # 장바구니 라벨
        cart_label = QLabel("장바구니")
        cart_label.setFont(QFont("Arial", 16))
        cart_label.setAlignment(Qt.AlignCenter)
        cart_layout.addWidget(cart_label)

        # 장바구니 리스트
        self.cart_list = QWidget()
        self.cart_list_layout = QVBoxLayout()
        self.cart_list_layout.setAlignment(Qt.AlignTop)
        self.cart_list.setLayout(self.cart_list_layout)
        cart_scroll_area = QScrollArea()
        cart_scroll_area.setWidgetResizable(True)
        cart_scroll_area.setWidget(self.cart_list)
        cart_scroll_area.setFixedHeight(250)  # 장바구니 리스트 높이 조정
        cart_layout.addWidget(cart_scroll_area)

        # 합계 금액
        self.cart_total_label = QLabel("합계: 0원")
        self.cart_total_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.cart_total_label.setStyleSheet("""
            QLabel {
                color: black;
                background-color: #f5f5f5;
                border: 2px solid #dcdcdc;
                border-radius: 10px;
                padding: 10px;
                qproperty-alignment: 'AlignCenter';
            }
        """)
        cart_layout.addWidget(self.cart_total_label, alignment=Qt.AlignRight)

        # Spacer 추가로 결제 버튼을 하단 고정
        cart_layout.addStretch()

        # 결제 버튼
        pay_button = QPushButton("결제하기")
        pay_button.setFixedSize(150, 50)
        pay_button.setFont(QFont("Arial", 14))
        pay_button.setStyleSheet("""
            QPushButton {
                background-color: #0099cc;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #0077aa;
            }
        """)
        pay_button.clicked.connect(self.show_payment_popup)
        cart_layout.addWidget(pay_button, alignment=Qt.AlignRight)

        # 오른쪽 레이아웃 추가
        main_layout.addLayout(cart_layout, stretch=1)

        self.setCentralWidget(main_widget)

        # 카테고리 및 메뉴 생성
        self.populate_menu(categories)




    def show_staff_call_popup(self):
        # 직원 호출 팝업 생성
        popup = QDialog(self)
        popup.setWindowTitle("직원 호출")
        popup_layout = QVBoxLayout()
        popup.setLayout(popup_layout)

        # 팝업 메시지
        message_label = QLabel("직원이 호출되었습니다.")
        message_label.setFont(QFont("Arial", 14))
        message_label.setAlignment(Qt.AlignCenter)
        popup_layout.addWidget(message_label)

        # 확인 버튼
        close_button = QPushButton("확인")
        close_button.setFont(QFont("Arial", 12))
        close_button.clicked.connect(popup.close)
        popup_layout.addWidget(close_button, alignment=Qt.AlignCenter)

        popup.exec_()

    def populate_menu(self, categories):
        for category, count in categories.items():
            # 카테고리 라벨 추가
            category_label = QLabel(category)
            category_label.setFont(QFont("Arial", 14))
            category_label.setAlignment(Qt.AlignCenter)
            self.menu_layout.addWidget(category_label)

            # 카테고리 위치 저장
            self.category_positions[category] = category_label

            # 메뉴 항목 추가
            item_grid = QGridLayout()
            for i in range(count):
                item_frame = QFrame()
                item_frame.setFrameShape(QFrame.StyledPanel)
                item_layout = QVBoxLayout()
                item_frame.setLayout(item_layout)
                item_frame.setStyleSheet("""
                    QFrame {
                        border: 2px solid #cccccc;
                        border-radius: 10px;
                        background-color: #ffffff;
                    }
                """)

                # 이미지 추가
                image_label = QLabel()
                image_label.setFixedSize(200, 200)  # 메뉴 박스 크기 확대
                image_label.setStyleSheet("background-color: gray; border-radius: 10px;")
                item_layout.addWidget(image_label)

                # 랜덤으로 메뉴 가져오기
                menu_item = random.choice(self.menu_data)

                # 메뉴 이름과 가격
                item_name = QLabel(f"{menu_item['name']}")
                item_name.setAlignment(Qt.AlignCenter)
                item_name.setFont(QFont("Arial", 14))  # 글씨 크기 확대
                item_layout.addWidget(item_name)

                item_price = QLabel(f"{menu_item['price']}원")
                item_price.setAlignment(Qt.AlignCenter)
                item_price.setFont(QFont("Arial", 14))
                item_price.setStyleSheet("color: red; font-weight: bold;")
                item_layout.addWidget(item_price)

                # 선택 버튼
                select_button = QPushButton("선택")
                select_button.setFixedHeight(50)
                select_button.setFont(QFont("Arial", 12))
                select_button.setStyleSheet("""
                    QPushButton {
                        background-color: #e6f7ff;
                        color: #333333;
                        border-radius: 10px;
                    }
                    QPushButton:hover {
                        background-color: #cceeff;
                    }
                """)
                select_button.clicked.connect(
                    lambda _, price=menu_item['price'], name=menu_item['name']: self.add_to_cart(name, price)
                )
                item_layout.addWidget(select_button)

                item_grid.addWidget(item_frame, i // 3, i % 3)

            self.menu_layout.addLayout(item_grid)

    def scroll_to_category(self, category):
        if category in self.category_positions:
            category_widget = self.category_positions[category]
            scroll_position = category_widget.pos().y()
            self.scroll_area.verticalScrollBar().setValue(scroll_position)

    def add_to_cart(self, name, price):
        if name in self.cart_items:
            self.cart_items[name]['quantity'] += 1
        else:
            self.cart_items[name] = {'price': price, 'quantity': 1}
        self.update_cart_ui()

    def update_cart_ui(self):
        self.cart_total = 0

        for i in reversed(range(self.cart_list_layout.count())):
            widget = self.cart_list_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        for name, details in reversed(list(self.cart_items.items())):
            cart_item_frame = QFrame()
            cart_item_layout = QVBoxLayout()
            cart_item_frame.setLayout(cart_item_layout)

            item_label = QLabel(f"{name}")
            item_label.setFont(QFont("Arial", 12))
            cart_item_layout.addWidget(item_label)

            price_label = QLabel(f"{details['price']}원")
            price_label.setFont(QFont("Arial", 14))
            price_label.setStyleSheet("color: red;")
            cart_item_layout.addWidget(price_label)

            button_layout = QHBoxLayout()
            minus_button = QPushButton("-")
            minus_button.setFixedSize(30, 30)
            minus_button.clicked.connect(lambda _, n=name: self.update_quantity(n, -1))
            button_layout.addWidget(minus_button)

            quantity_label = QLabel(f"{details['quantity']}")
            quantity_label.setAlignment(Qt.AlignCenter)
            button_layout.addWidget(quantity_label)

            plus_button = QPushButton("+")
            plus_button.setFixedSize(30, 30)
            plus_button.clicked.connect(lambda _, n=name: self.update_quantity(n, 1))
            button_layout.addWidget(plus_button)

            remove_button = QPushButton("삭제")
            remove_button.setFixedSize(50, 30)
            remove_button.clicked.connect(lambda _, n=name: self.remove_from_cart(n))
            button_layout.addWidget(remove_button)

            cart_item_layout.addLayout(button_layout)

            self.cart_list_layout.insertWidget(0, cart_item_frame)

            self.cart_total += details['price'] * details['quantity']

        self.cart_total_label.setText(f"합계: {self.cart_total}원")
        self.cart_total_label.setAlignment(Qt.AlignRight)

    def update_quantity(self, name, change):
        if name in self.cart_items:
            self.cart_items[name]['quantity'] += change
            if self.cart_items[name]['quantity'] <= 0:
                del self.cart_items[name]
        self.update_cart_ui()

    def remove_from_cart(self, name):
        if name in self.cart_items:
            del self.cart_items[name]
        self.update_cart_ui()

    def show_payment_popup(self):
        popup = QDialog(self)
        popup.setWindowTitle("결제 확인")
        popup_layout = QVBoxLayout()
        popup.setLayout(popup_layout)

        title = QLabel("장바구니의 상품과 수량을 확인하셨습니까?")
        title.setFont(QFont("Arial", 14))
        title.setAlignment(Qt.AlignCenter)
        popup_layout.addWidget(title)

        for name, details in self.cart_items.items():
            item_label = QLabel(f"{name}: {details['quantity']}개 - {details['price']}원")
            popup_layout.addWidget(item_label)

        total_label = QLabel(f"합계: {self.cart_total}원")
        total_label.setFont(QFont("Arial", 12))
        total_label.setStyleSheet("color: red;")
        popup_layout.addWidget(total_label)

        button_layout = QHBoxLayout()
        cancel_button = QPushButton("취소")
        cancel_button.clicked.connect(popup.close)
        button_layout.addWidget(cancel_button)

        pay_button = QPushButton("결제하기")
        pay_button.setStyleSheet("background-color: red; color: white;")
        pay_button.clicked.connect(lambda: print("결제가 완료되었습니다!"))
        button_layout.addWidget(pay_button)

        popup_layout.addLayout(button_layout)

        popup.exec_()


def main():
    app = QApplication(sys.argv)
    window = MenuApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
