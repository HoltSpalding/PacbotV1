#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def gameState_publisher():
    pub = rospy.Publisher('/gameState', String, queue_size=10)
    rospy.init_node('gameState_pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        gameState_publisher()
    except rospy.ROSInterruptException:
        pass
