
import rospy
from geometry_msgs.msg import Twist
from enum import Enum

class Direction(Enum):
    forward = "forward"
    backward = "backward"
    c_rotate = "clockwise_rotate"
    cc_rotate = "countclockwise_rotate"

#abstraction for twist message
def pubTwistMsg(direction = foward, linear_units = 1.0, angle = 90)
    if not isinstance(direction, Direction):
        raise TypeError('direction must be an instance of Direction Enum')
    vel_msg = Twist()

    if (direction = forward):
        vel_msg.linear.x = linear_units
    if (direction = backward):
        vel_msg.linear.x = -linear_units
    if (direction = c_rotate):
        vel_msg.angular.z = angle
    if (direction = cc_rotate):
        vel_msg.angular.z = -angle
    return vel_msg
    