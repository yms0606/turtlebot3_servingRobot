import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yms/rokey_week4_ws/turtlebot3_servingRobot/install/serving_node'
