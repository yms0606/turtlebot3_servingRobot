import rclpy
from rclpy.node import Node
from rclpy.qos import *
from rcl_interfaces.msg import Log
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from serving_interface.srv import ServingStatus
import math

qos_profile_pose = QoSProfile(
    history=QoSHistoryPolicy.KEEP_LAST, depth=10,     # 10개 정도의 데이터 유지
    reliability=QoSReliabilityPolicy.BEST_EFFORT,     # 속도 중시
    durability=QoSDurabilityPolicy.VOLATILE,          # 섭스크라이버 생선 전 데이터 무효
)

qos_profile_pub_pose = QoSProfile(
    history=QoSHistoryPolicy.KEEP_LAST, depth=10,
    reliability=QoSReliabilityPolicy.RELIABLE,
    durability=QoSDurabilityPolicy.VOLATILE
)



class TurtleBotClient(Node):
    def __init__(self):
        super().__init__('turtlebot_client')
        # Create service client
        self.client = self.create_client(ServingStatus, 'serving_status')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Waiting for Table Order Server...')
        self.get_logger().info('Connected to Table Order Server!')

        self.req = ServingStatus.Request()

        # Goal successed
        self.sub_current_status = self.create_subscription(
            Log, 'rosout', self.goal_status_callback, 10
        )

        self.x = 0.0
        self.y = 0.0
        self.initial_pose_sub = self.create_subscription(
            PoseWithCovarianceStamped, '/amcl_pose', self.amcl_pose_callback, qos_profile=qos_profile_pose)


        #초기 위치로
        self.pub_initial_pose = self.create_publisher(PoseStamped, '/goal_pose', qos_profile=qos_profile_pub_pose)
        self.initial_pose = PoseStamped()
        self.initial_pose.header.frame_id = "map"
        self.initial_pose.pose.position.x = 0.0
        self.initial_pose.pose.position.y = 0.0
        self.initial_pose.pose.orientation.z = 0.0
        self.initial_pose.pose.orientation.w = 0.0

        self.to_initial_pose()


        # self.sub_current_pose = self.create_subscription(
        #     Odometry, '/odom', self.odom_callback, 10
        # )
        # self.current_position = None  # To store the current position of the robot

        # # Table positions (x, y) for each table (from the provided data)
        # self.table_positions = {
        #     1: (1.28, 1.60, 0.99, 0.02),
        #     2: (1.30, 0.49, -0.99, 0.02),
        #     3: (1.31, -0.49, -0.66, 0.74),
        #     4: (2.48, 1.65, -0.99, 0.11),
        #     5: (2.46, 0.51, -0.99, 0.02),
        #     6: (2.41, -0.62, -0.99, 0.01),
        #     7: (3.65, 1.61, -0.99, 0.06),
        #     8: (3.91, 0.51, 0.99, 0.02),
        #     9: (3.76, -0.67, -0.99, 0.0)
        # }

        # # Offset to convert RViz coordinates to TurtleBot's coordinates
        # self.destination_offset = (-2.0, -1.0)  # Example offset, adjust based on your setup

        # # Example: Set the destination to table 3 (you can change the table number)
        # self.destination_table = 3
        
        # self.update_destination()
    def goal_status_callback(self, msg):
        
        if "Goal succeeded" in msg.msg:
            self.get_logger().info("arrvied goal")

            if abs(self.x) < 0.5 and abs(self.y) < 0.5:
                self.get_logger().info("arrived initial pose")
            else:
                self.get_logger().info("arrived table")
                self.send_goal_status(True)
        #else:
        #    self.get_logger().error('Service call failed: goal_status_callback')
    
    def send_goal_status(self, is_arrived):
        self.req.is_arrived = is_arrived
        self.future = self.client.call_async(self.req)
        self.future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        if future.result():
            response = future.result()
            if response.get_back:
                self.get_logger().info("go to initial pose")
                self.to_initial_pose()
            else:
                self.get_logger().error('Service call failed: response_callback')

    def to_initial_pose(self):
        self.get_logger().info("moving . . . ")
        self.initial_pose.header.stamp = self.get_clock().now().to_msg()
        self.pub_initial_pose.publish(self.initial_pose)

    def amcl_pose_callback(self,msg):
        pose_msg = msg
        self.x = pose_msg.pose.pose.position.x
        self.y = pose_msg.pose.pose.position.y
        self.get_logger().debug(f"{self.x},{self.y}")

    # def update_destination(self):
    #     """Update the destination by applying the offset."""
    #     original_pos = self.table_positions[self.destination_table]
    #     self.destination_rviz = (
    #         original_pos[0] + self.destination_offset[0],
    #         original_pos[1] + self.destination_offset[1]
    #     )

    # def odom_callback(self, msg):
    #     """Callback to update the current position of the robot."""
    #     self.current_position = (
    #         msg.pose.pose.position.x,
    #         msg.pose.pose.position.y
    #     )

    # def is_at_destination(self):
    #     """Check if the robot is at the destination."""
    #     if self.current_position is None:
    #         return False
    #     dest_x, dest_y = self.destination_rviz
    #     current_x, current_y = self.current_position
    #     distance = math.sqrt((current_x - dest_x)**2 + (current_y - dest_y)**2)
    #     self.get_logger().info(f'Distance to destination: {distance}')
    #     return distance < 0.6  # Threshold for arrival (in meters)

    def send_request(self):
        """Send the arrival status to the server."""
        request = ServingStatus.Request()
        request.is_arrived = self.is_at_destination()
        self.get_logger().info(f'Sending is_arrived={request.is_arrived} to server...')
        self.future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()



def main(args=None):
    rclpy.init(args=args)
    client = TurtleBotClient()

    while rclpy.ok():
        rclpy.spin_once(client)
        
    rclpy.shutdown()


if __name__ == '__main__':
    main()
