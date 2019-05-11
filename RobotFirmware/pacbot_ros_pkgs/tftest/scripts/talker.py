#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from enum import Enum

UNITS = 0.7 #1 unit is 7 inches

########direction abstraction#########
class Direction(Enum):
    forward = "forward"
    backward = "backward"
    c_rotate = "clockwise_rotate"
    cc_rotate = "countclockwise_rotate"

#abstraction for twist message
def pubTwistMsg(direction = foward, val = 1.0)
    if not isinstance(direction, Direction):
        raise TypeError('direction must be an instance of Direction Enum')
    vel_msg = Twist()
    if (direction == forward or direction == backward):
        val *= UNITS

    if (direction = forward):
        vel_msg.linear.x = val
    if (direction = backward):
        vel_msg.linear.x = -val
    if (direction = c_rotate):
        vel_msg.angular.z = val
    if (direction = cc_rotate):
        vel_msg.angular.z = -val
    return vel_msg
########direction abstraction#########


def cmd_vel_publisher():
    pub = rospy.Publisher('/trin_base_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('cmd_vel_publisher', anonymous=True)
    vel_msg = Twist()
    rate = rospy.Rate(10) # 10hz, TBD we're getting messages at 30hz i think



    while not rospy.is_shutdown():
        #pubTwistMsg(forward, 1.0) 
        # pubTwistMsg(c_rotate,90)
       

        vel_msg.linear.x = 1.0
        vel_msg.linear.y = 1.0
        # rospy.loginfo("Test")
        pub.publish(vel_msg)
        rate.sleep()




def odom_listener():
    rospy.init_node('odom_listener', anonymous=True)
    rospy.Subscriber("/trin_base_controller/odom", Odometry, queue_size = 10)
    rospy.spin()

if __name__ == '__main__':
    try:
        cmd_vel_publisher()
        odom_listener()
    except rospy.ROSInterruptException:
        pass