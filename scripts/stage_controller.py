#! /usr/bin/env python3

import rospy 
import math
import rospy

from nav_msgs.msg import *
from sensor_msgs.msg import *
from geometry_msgs.msg import *

def odometry_callback(data):
    global odometry
    odometry = data
    
def laser_callback(data):
    global laser
    laser = data

def obstacle_avoidance():
    x = odometry.pose.pose.position.x
    y = odometry.pose.pose.position.y

    obstacle_threshold = 0.5
    max_linear_velocity = 0.25  # Velocidade linear máxima permitida
    max_angular_velocity = 0.25  # Velocidade angular máxima permitida

    rospy.loginfo("Where I am: X: %s, Y: %s", x, y)

    if (len(laser.ranges) > 0):
        if (min(laser.ranges) > obstacle_threshold):
            #velocity.linear.x = 0.25
            #velocity.angular.z = random.uniform(-0.25, 0.25)
            min_range_idx = laser.ranges.index(min(laser.ranges))
            angle_to_obstacle = laser.angle_min + min_range_idx * laser.angle_increment

            # Calcula as velocidades lineares e angulares desejadas
            velocity.linear.x = max_linear_velocity * (1 - min(laser.ranges) / obstacle_threshold)
            velocity.angular.z = max_angular_velocity * (angle_to_obstacle / abs(angle_to_obstacle))
        else:
            velocity.linear.x = 0.0
            velocity.angular.z = 0.25
        pub.publish(velocity)

if __name__ == "__main__": 
    rospy.init_node("stage_controller_node", anonymous=False)

    rospy.Subscriber("/base_pose_ground_truth", Odometry, odometry_callback)
    rospy.Subscriber("/base_scan", LaserScan, laser_callback)

    # Definindo o tipo de mensagem das variáveis
    laser = LaserScan()
    odometry = Odometry()

    target_x = 1.0
    target_y = 2.0
    min_distance = 0.1

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)    
    r = rospy.Rate(5) # 5Hz
    
    velocity = Twist()

    while not rospy.is_shutdown():
        x = odometry.pose.pose.position.x
        y = odometry.pose.pose.position.y
        
        # Verifica se chegou ao alvo
        distance = math.sqrt((x - target_x)** 2 + (y - target_y)** 2)

        if (distance > min_distance):
            obstacle_avoidance()  # Chamada para a função de desvio de obstáculos
        else:
            velocity.linear.x = 0.0
            velocity.angular.z = 0.0
            pub.publish(velocity)
            rospy.loginfo("Alvo Alcancado!!!!!")         
        r.sleep()