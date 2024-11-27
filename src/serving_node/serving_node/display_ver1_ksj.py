from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QMainWindow, QDialog
from PyQt5.QtCore import Qt
import sys

class KitchenDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.orders = []  # 주문 데이터 리스트 (테이블 번호와 메뉴)
        self.completed_orders = []  # 출발된 메뉴 데이터
        self.total_price = 0  # 총 주문 가격 (정산용)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("주방 디스플레이")
        self.setGeometry(100, 100, 800, 600)

        # 메인 레이아웃
        self.main_layout = QVBoxLayout()

        # 각 줄 레이아웃
        self.table_layout = QHBoxLayout()  # 테이블 번호
        self.pending_menu_layout = QHBoxLayout()  # 조리할 메뉴
        self.completed_menu_layout = QHBoxLayout()  # 조리 완료된 메뉴
        self.buttons_layout = QHBoxLayout()  # 버튼

        # 테이블 번호 초기화 (순서대로 왼쪽 칸에 배치)
        for _ in range(5):
            label = QLabel("대기 중")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 16px; color: #333; padding: 10px; background-color: #f9f9f9; "
                                "border: 1px solid #ddd; border-radius: 5px; font-weight: bold;")
            self.table_layout.addWidget(label)

        # 조리할 메뉴 초기화
        for i in range(5):
            label = QLabel("대기 중")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 16px; color: #666; padding: 10px; background-color: #fff; "
                                "border: 1px solid #ddd; border-radius: 5px;")
            # 클릭 시 완료 처리
            label.mousePressEvent = lambda event, idx=i: self.complete_order(idx)
            self.pending_menu_layout.addWidget(label)

        # 조리 완료된 메뉴 초기화
        for _ in range(5):
            label = QLabel("대기 중")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 16px; color: #666; padding: 10px; background-color: #fff; "
                                "border: 1px solid #ddd; border-radius: 5px;")
            self.completed_menu_layout.addWidget(label)

        # 하단 버튼
        for i in range(4):
            button = QPushButton("출발")
            button.setEnabled(False)  # 처음에는 비활성화 상태
            button.clicked.connect(lambda _, idx=i: self.start_robot(idx))
            button.setStyleSheet("background-color: #FF5722; color: white; font-size: 14px; padding: 10px; "
                                 "border-radius: 5px; margin: 5px;")
            self.buttons_layout.addWidget(button)

        # 우측 하단에 정산하기 버튼 추가
        settle_button = QPushButton("정산하기")
        settle_button.clicked.connect(self.show_settlement)
        settle_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 14px; padding: 10px; "
                                    "border-radius: 5px; margin: 5px;")
        self.buttons_layout.addWidget(settle_button)

        # 레이아웃을 메인 레이아웃에 추가
        self.main_layout.addLayout(self.table_layout)
        self.main_layout.addLayout(self.pending_menu_layout)
        self.main_layout.addLayout(self.completed_menu_layout)
        self.main_layout.addLayout(self.buttons_layout)

        self.setLayout(self.main_layout)

    def add_order(self, table_number, menu, price):
        """
        새로운 주문을 추가합니다.
        """
        if len(self.orders) >= 5:
            print("최대 5개의 주문만 표시 가능합니다.")
            return

        # 주문 데이터 저장
        self.orders.append((table_number, menu, price))
        self.total_price += price

        # 테이블 번호 업데이트 (순서대로 왼쪽 칸에 배치)
        self.table_layout.itemAt(len(self.orders) - 1).widget().setText(f"테이블 {table_number}")

        # 조리할 메뉴 업데이트
        self.pending_menu_layout.itemAt(len(self.orders) - 1).widget().setText(menu)

    def complete_order(self, index):
        """
        조리가 완료된 주문을 처리합니다.
        """
        if index >= len(self.orders):
            return

        table_number, menu, _ = self.orders[index]
        self.completed_menu_layout.itemAt(index).widget().setText(menu)  # 조리 완료 표시

        # 조리 중인 메뉴 비우기
        self.pending_menu_layout.itemAt(index).widget().setText("완료")

        # 해당 테이블의 출발 버튼 색상을 변경
        self.check_all_completed(index)

    def start_robot(self, index):
        """
        출발 버튼 클릭 시 호출, 해당 테이블로 로봇을 출발시킵니다.
        """
        if index >= len(self.orders):
            print("해당 칸에 주문이 없습니다.")
            return

        table_number, menu, _ = self.orders[index]

        # 출발 버튼 비활성화 및 색상 변경
        self.buttons_layout.itemAt(index).widget().setEnabled(False)
        self.buttons_layout.itemAt(index).widget().setStyleSheet("background-color: #FF5722; color: white; "
                                                                "font-size: 14px; padding: 10px; border-radius: 5px; "
                                                                "margin: 5px;")  # 빨간색

        # 해당 주문을 출발 처리 (삭제하지 않고 completed_orders에 추가)
        self.completed_orders.append(self.orders[index])

        # 주문에서 해당 항목 삭제
        self.orders.pop(index)

        # 상태 초기화 후, 나머지 주문을 왼쪽으로 시프트
        self.update_orders()

        # 출발 버튼 위의 칸들(테이블 번호, 메뉴)을 함께 왼쪽으로 시프트
        self.shift_up(index)

    def shift_up(self, index):
        """
        출발된 주문의 인덱스에 맞춰 버튼 위의 칸들(테이블 번호, 메뉴)을 왼쪽으로 시프트합니다.
        """
        # 테이블 번호, 조리할 메뉴, 완료된 메뉴 모두 왼쪽으로 시프트
        for layout in [self.table_layout, self.pending_menu_layout, self.completed_menu_layout]:
            layout.itemAt(index).widget().setText("대기 중")  # 이동된 칸을 초기화

        # 나머지 주문을 왼쪽으로 시프트
        for i in range(index, len(self.orders)):
            # 테이블 번호와 메뉴를 업데이트
            self.table_layout.itemAt(i).widget().setText(f"테이블 {self.orders[i][0]}")
            self.pending_menu_layout.itemAt(i).widget().setText(self.orders[i][1])
            self.completed_menu_layout.itemAt(i).widget().setText("대기 중")

        # 남은 공간은 초기화
        for layout in [self.table_layout, self.pending_menu_layout, self.completed_menu_layout]:
            for i in range(len(self.orders), 5):
                layout.itemAt(i).widget().setText("대기 중")


    def update_orders(self):
        """
        주문 데이터를 UI와 동기화합니다.
        """
        for i, (table_number, menu, _) in enumerate(self.orders):
            self.table_layout.itemAt(i).widget().setText(f"테이블 {table_number}")
            self.pending_menu_layout.itemAt(i).widget().setText(menu)

        # 나머지 칸은 초기화
        for i in range(len(self.orders), 5):
            self.table_layout.itemAt(i).widget().setText("대기 중")
            self.pending_menu_layout.itemAt(i).widget().setText("대기 중")
            self.completed_menu_layout.itemAt(i).widget().setText("대기 중")

    def check_all_completed(self, index):
        """
        해당 테이블의 주문이 모두 조리 완료되었는지 확인하고 출발 버튼 색상을 변경합니다.
        """
        all_completed = all(label.text() != "대기 중" for label in self.pending_menu_layout.children())
        if all_completed:
            self.buttons_layout.itemAt(index).widget().setStyleSheet("background-color: #4CAF50; color: white; "
                                                                    "font-size: 14px; padding: 10px; border-radius: 5px; "
                                                                    "margin: 5px;")  # 완료되면 색상 변경
            self.buttons_layout.itemAt(index).widget().setEnabled(True)  # 버튼 활성화

    def show_settlement(self):
        """
        정산하기 버튼을 눌렀을 때 호출, 총 주문 내역과 가격을 표시합니다.
        """
        # 정산 내역을 새로운 창에서 표시
        settlement_window = SettlementWindow(self.orders, self.completed_orders, self.total_price)
        settlement_window.exec_()


class SettlementWindow(QDialog):  # QMainWindow -> QDialog로 변경
    def __init__(self, orders, completed_orders, total_price):
        super().__init__()
        self.orders = orders
        self.completed_orders = completed_orders
        self.total_price = total_price
        self.setWindowTitle("정산 내역")
        self.setGeometry(200, 200, 400, 300)

        # 테이블 및 메뉴 내용 표시
        table_widget = QTableWidget(self)
        table_widget.setRowCount(len(self.orders) + len(self.completed_orders))
        table_widget.setColumnCount(3)
        table_widget.setHorizontalHeaderLabels(["테이블", "메뉴", "가격"])

        # 주문 목록 표시
        row = 0
        for table_number, menu, price in self.orders:
            table_widget.setItem(row, 0, QTableWidgetItem(str(table_number)))
            table_widget.setItem(row, 1, QTableWidgetItem(menu))
            table_widget.setItem(row, 2, QTableWidgetItem(str(price)))
            row += 1

        # 출발된 주문 추가
        for table_number, menu, price in self.completed_orders:
            table_widget.setItem(row, 0, QTableWidgetItem(str(table_number)))
            table_widget.setItem(row, 1, QTableWidgetItem(menu))
            table_widget.setItem(row, 2, QTableWidgetItem(str(price)))
            row += 1

        # 총액 표시
        total_label = QLabel(f"총액: {self.total_price} 원", self)

        layout = QVBoxLayout()
        layout.addWidget(table_widget)
        layout.addWidget(total_label)

        container = QWidget()
        container.setLayout(layout)
        self.setLayout(layout)  # QDialog는 setLayout을 사용해야 함


if __name__ == '__main__':
    app = QApplication(sys.argv)
    kitchen_display = KitchenDisplay()
    kitchen_display.show()

    # 예시 주문 추가
    kitchen_display.add_order(1, "김치찌개", 8000)
    kitchen_display.add_order(2, "된장찌개", 7500)
    kitchen_display.add_order(3, "비빔밥", 9500)
    kitchen_display.add_order(4, "김치찌개", 8000)
    kitchen_display.add_order(5, "된장찌개", 7500)
    kitchen_display.add_order(6, "비빔밥", 9500)

    sys.exit(app.exec_())