import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/juna/doosan_boot_work/driving1/turtlebot3_servingRobot/install/serving_node'
