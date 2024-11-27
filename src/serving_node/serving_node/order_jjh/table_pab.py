import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QGridLayout, QScrollArea, QWidget, QTableWidget, QTableWidgetItem, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class TableOrderApp(QMainWindow):
    def __init__(self, menu_files):
        super().__init__()
        self.setWindowTitle("부리부리대마왕포차")
        self.setGeometry(100, 100, 1200, 800)

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
        table_label.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
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
            button.clicked.connect(lambda _, cat=category: self.show_category_menu(cat))
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
        self.menu_layout = QGridLayout()
        self.menu_layout.setSpacing(10)
        menu_widget = QWidget()
        menu_widget.setLayout(self.menu_layout)
        menu_scroll = QScrollArea()
        menu_scroll.setWidget(menu_widget)
        menu_scroll.setWidgetResizable(True)
        menu_scroll.setStyleSheet("border-right: 2px solid #ccc;")

        # 기본적으로 첫 번째 카테고리 표시
        first_category = list(self.menu_data.keys())[0]
        self.show_category_menu(first_category)

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
        self.total_label.setStyleSheet("font-size: 16px; padding: 10px;")
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
        center_layout.addWidget(menu_scroll)  # 중앙 메뉴
        center_layout.addWidget(right_frame)  # 오른쪽 장바구니

        main_layout.addLayout(center_layout)

    def call_staff(self):
        """직원 호출 버튼 클릭 시 팝업 표시"""
        message_box = QMessageBox()
        message_box.setWindowTitle("직원 호출")
        message_box.setText("직원이 호출되었습니다!")
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def load_menu_data(self, menu_files):
        """메뉴 파일에서 카테고리와 메뉴 데이터를 로드"""
        menu_data = {}
        for file in menu_files:
            category = os.path.splitext(os.path.basename(file))[0]  # 파일 이름을 카테고리로
            menu_data[category] = []
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()  # 양쪽 공백 제거
                    if not line:  # 빈 줄 무시
                        continue
                    try:
                        name, price = line.split(" - ")
                        menu_data[category].append((name, int(price)))
                    except ValueError:
                        print(f"잘못된 데이터 무시: {line}")
                        continue
        return menu_data

    def show_category_menu(self, category):
        """선택된 카테고리의 메뉴를 표시"""
        self.current_category = category

        # 기존 메뉴 지우기
        for i in reversed(range(self.menu_layout.count())):
            self.menu_layout.itemAt(i).widget().deleteLater()

        # 새로운 메뉴 추가
        for index, (menu_name, price) in enumerate(self.menu_data[category]):
            # 메뉴 카드 생성
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

            # 메뉴 이미지 (이미지 크기를 키움)
            image_label = QLabel()
            image_path = f"./images/{menu_name}.png"
            if os.path.exists(image_path):
                pixmap = QPixmap(image_path).scaled(160, 100, Qt.KeepAspectRatio)  # 이미지를 좀 더 크게
            else:
                pixmap = QPixmap(160, 100)  # 기본 빈 이미지
                pixmap.fill(Qt.lightGray)
            image_label.setPixmap(pixmap)
            image_label.setAlignment(Qt.AlignCenter)

            # 메뉴 이름과 가격 (텍스트 크기 줄이기)
            name_label = QLabel(menu_name)
            name_label.setAlignment(Qt.AlignCenter)
            name_label.setStyleSheet("font-size: 12px; font-weight: bold; margin: 5px;")

            price_label = QLabel(f"{price}원")
            price_label.setAlignment(Qt.AlignCenter)
            price_label.setStyleSheet("font-size: 12px; color: #333; margin-bottom: 10px;")

            # 카드 구성
            card_layout.addWidget(image_label)
            card_layout.addWidget(name_label)
            card_layout.addWidget(price_label)

            # 카드 클릭 이벤트
            card.mousePressEvent = lambda _, n=menu_name, p=price: self.add_to_cart(n, p)

            # 카드 추가
            row, col = divmod(index, 3)  # 한 줄에 3개씩
            self.menu_layout.addWidget(card, row, col)

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

            self.cart_table.setItem(row, 0, QTableWidgetItem(name))

            # 수량 조정 버튼과 수량 표시
            quantity_layout = QHBoxLayout()
            minus_button = QPushButton("-")
            minus_button.setStyleSheet("font-size: 20px; padding: 15px;")
            minus_button.clicked.connect(lambda _, n=name: self.decrease_quantity(n))

            quantity_label = QLabel(f"{data['quantity']}")
            quantity_label.setStyleSheet("font-size: 15px; padding: 4px;")
            plus_button = QPushButton("+")
            plus_button.setStyleSheet("font-size: 20px; padding: 15px;")
            plus_button.clicked.connect(lambda _, n=name: self.increase_quantity(n))

            # 수량 버튼과 텍스트 배치
            quantity_layout.addWidget(minus_button)
            quantity_layout.addWidget(quantity_label)
            quantity_layout.addWidget(plus_button)

            # 수량 버튼을 셀에 추가
            quantity_widget = QWidget()
            quantity_widget.setLayout(quantity_layout)
            self.cart_table.setCellWidget(row, 1, quantity_widget)

            # 현재 가격 표시
            total_price = data['price'] * data['quantity']
            self.cart_table.setItem(row, 2, QTableWidgetItem(f"{total_price}원"))

            self.cart_table.setRowHeight(row, 40)  # 적절한 높이 값으로 설정

        self.total_label.setText(f"총 금액: {total}원")

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


if __name__ == "__main__":
    menu_files = ["메인 메뉴.txt", "사이드 메뉴.txt", "주류 및 음료.txt"]
    app = QApplication(sys.argv)
    window = TableOrderApp(menu_files)
    window.show()
    sys.exit(app.exec_())
