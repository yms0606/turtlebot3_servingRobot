import rclpy
from rclpy.node import Node
from serving_interface.srv import ServingStatus


class TurtlebotNode(Node):
    """터틀봇 노드 클래스: 테이블 오더와 통신하는 클라이언트"""

    def __init__(self):
        super().__init__('turtlebot_node')
        # 서비스 클라이언트 생성 (서비스 이름: 'serving_status')
        self.client = self.create_client(ServingStatus, 'serving_status')

        # 서비스 연결 확인
        while not self.client.wait_for_service(timeout_sec=5.0):
            self.get_logger().info('테이블 오더 서비스 연결 대기 중...')

        # 터틀봇이 도착했음을 알리고 복귀 여부를 요청
        self.send_request()

    def send_request(self):
        """서비스 요청을 생성하고 전송"""
        # 서비스 요청 메시지 생성
        request = ServingStatus.Request()
        request.is_arrived = True  # 터틀봇이 목적지(테이블)에 도착했음을 알림

        self.future = self.client.call_async(request)  # 비동기 서비스 호출
        self.future.add_done_callback(self.response_callback)  # 응답 콜백 함수 연결

    def response_callback(self, future):
        """서비스 응답 처리 콜백 함수"""
        try:
            response = future.result()  # 서비스 응답 결과 가져오기
            if response.get_back:  # 복귀 명령 여부 확인
                self.get_logger().info("복귀 명령을 수신했습니다. 초기 위치로 복귀합니다...")
                self.return_to_initial_position()  # 복귀 로직 수행
            else:
                self.get_logger().info("복귀 명령 없음. 대기 상태 유지...")
        except Exception as e:
            self.get_logger().error(f"서비스 호출 중 오류 발생: {e}")

    def return_to_initial_position(self):
        """초기 위치로 복귀하는 로직"""
        # 여기에 실제 초기 위치로 복귀하는 로직을 추가할 수 있습니다.
        self.get_logger().info("터틀봇이 초기 위치로 복귀 중입니다...")
        # ROS2 Navigation 또는 모터 제어 명령을 호출하여 복귀를 구현해야 합니다.
        pass


def main(args=None):
    """터틀봇 노드 실행"""
    rclpy.init(args=args)
    node = TurtlebotNode()

    try:
        # 노드 실행
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # 노드 종료 및 ROS2 종료
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
