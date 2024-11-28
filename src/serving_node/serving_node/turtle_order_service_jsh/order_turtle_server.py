import rclpy
from rclpy.node import Node
from serving_interface.srv import ServingStatus
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class TableOrderNode(Node):
    def __init__(self):
        super().__init__('table_order_node')
        self.srv = self.create_service(ServingStatus, 'serving_status', self.handle_request)
        self.robot_arrived = False

    def handle_request(self, request, response):
        """서비스 요청 처리"""
        if request.is_arrived:
            self.robot_arrived = True
            self.get_logger().info("터틀봇이 도착했습니다.")
            
            # 팝업을 표시하고 버튼의 결과를 가져옵니다
            user_button = self.show_popup()
            response.get_back = user_button  # 복귀 버튼 클릭 여부 반환
        else:
            response.get_back = False
        return response

    def show_popup(self):
        """PyQt5 팝업 표시"""
        popup = QDialog()
        popup.setWindowTitle("메뉴 수령")
        popup.setFixedSize(500, 400)

        popup_layout = QVBoxLayout()
        popup.setLayout(popup_layout)

        # 제목 라벨
        title = QLabel("터틀봇이 도착했습니다.\n물건을 수령하세요.")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 25px; font-weight: bold; color: red;")
        popup_layout.addWidget(title)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()

        # 복귀 버튼
        return_button = QPushButton("복귀")
        return_button.setStyleSheet("font-size: 20px; background-color: green; color: white;")
        button_layout.addWidget(return_button)

        # 버튼 클릭 이벤트
        return_button.clicked.connect(lambda: popup.done(1))  # 버튼 클릭 시 팝업 닫고 결과 1 반환

        popup_layout.addLayout(button_layout)

        result = popup.exec_()  # 팝업 실행
        return result == 1  # 복귀 버튼을 클릭하면 True 반환


def main(args=None):
    rclpy.init(args=args)

    # PyQt5 애플리케이션 생성
    app = QApplication([])

    # ROS2 노드 생성
    node = TableOrderNode()

    try:
        # PyQt5와 ROS2 이벤트 루프를 통합
        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.1)
            app.processEvents()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
