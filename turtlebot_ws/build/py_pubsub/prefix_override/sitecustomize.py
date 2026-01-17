import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/liam-bouffard/Desktop/rob599_mobile_robotics/w1_ws/install/py_pubsub'
