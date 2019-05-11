#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry 
import math
import tf

RATE = 30 #
kp = 5
unit = 0.1778

class pacMove:
    def __init__(self):
        rospy.init_node('pac_move', anonymous=True)
        self.vel_pub = rospy.Publisher('/trin_base_controller/cmd_vel', Twist, queue_size=0)
        self.od_sub = rospy.Subscriber("/trin_base_controller/odom", Odometry, self.callback)
        self.current = Odometry().pose.pose
        rospy.rostime.wallsleep(0.6)

    def callback(self, dat):
        self.current = dat.pose.pose

    def move(self, distance):
        rate = rospy.Rate(RATE)
        vel_msg = Twist()
        vel_msg.linear.x = 0.30
        if (distance < 0):
            vel_msg.linear.x = -0.30
        initial_x = self.current.position.x
        initial_y = self.current.position.y
        print(initial_x, initial_y)
        travelled = 0
        while(travelled < abs(distance)):
            travelled = math.sqrt((self.current.position.x - initial_x)**2 + (self.current.position.y - initial_y)**2)
            print(travelled)
            self.vel_pub.publish(vel_msg)
            rate.sleep()

        vel_msg.linear.x = 0
        self.vel_pub.publish(vel_msg)

    def turn_left(self):
        rate = rospy.Rate(RATE)
        vel_msg = Twist()
        vel_msg.angular.z = 2
        for i in range(29):
            self.vel_pub.publish(vel_msg)
            rate.sleep()
        vel_msg.angular.z = 0
        self.vel_pub.publish(vel_msg)

    def turn_right(self):
        rate = rospy.Rate(RATE)
        vel_msg = Twist()
        vel_msg.angular.z = -2
        for i in range(34):
            self.vel_pub.publish(vel_msg)
            rate.sleep()
        vel_msg.angular.z = 0
        self.vel_pub.publish(vel_msg)


        # quaternion = (
        #     self.current.orientation.x,
        #     self.current.orientation.y,
        #     self.current.orientation.z,
        #     self.current.orientation.w)
        # initial_a = tf.transformations.euler_from_quaternion(quaternion)[2]
        # initial_a = initial_a + math.pi
        # angle = (initial_a + angle) % (2*math.pi)
        # print(angle)
        # for i in range(200):
        #     quaternion = (
        #         self.current.orientation.x,
        #         self.current.orientation.y,
        #         self.current.orientation.z,
        #         self.current.orientation.w)
        #     current_angle = tf.transformations.euler_from_quaternion(quaternion)
        #     # print(current_angle[2])
        #     vel_msg.angular.z = kp * (angle - current_angle[2] + math.pi)
        #     self.vel_pub.publish(vel_msg)
        #     if (vel_msg.angular.z < 0.35 and vel_msg.angular.z > -0.35):
        #         break
        #     rate.sleep()

        # vel_msg.angular.z = 0
        # self.vel_pub.publish(vel_msg)
        # exit(0)


if __name__ == '__main__':
    try:
        a = pacMove()
        a.move(7 * unit)
        a.turn_right()
        a.move(3 * unit)
        a.turn_left()
        a.move(3 * unit)
        a.turn_left()
        a.move(3 * unit)
        a.turn_right()
        a.move(2 * unit)
        a.turn_left()
        a.move(3 * unit)
        a.turn_left()
        a.move(11 * unit)
        a.turn_left()
        a.move(3 * unit)
        a.turn_right()
        a.move(9 * unit)
        a.turn_left()
        a.move(3 * unit)
        a.turn_right()
        # move()
    except KeyboardInterrupt: exit(0)
