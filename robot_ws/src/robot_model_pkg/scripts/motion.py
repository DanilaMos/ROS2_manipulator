#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from math import sin

def motion1():
    my_pub = rospy.Publisher('joint_states',JointState, queue_size=10)
    rospy.init_node('motion', anonymous=True) 
    rate_msg = rospy.Rate(15)
    robot_state = JointState()
    robot_state.header = Header()
    robot_state.header.stamp = rospy.Time.now()
    robot_state.name = ['base_to_link1', 'link1_to_link2', 'link2_to_dish'] 

    base_to_link1 = -3.14
    link1_to_link2 = -1.57
    link2_to_dish = -1.57
    
    my_pub.publish(robot_state)
    while not rospy.is_shutdown():	    
        robot_state.header.stamp = rospy.Time.now()
        robot_state.position = [base_to_link1, link1_to_link2, link2_to_dish]
        if -3.14 <= base_to_link1 <= 3.14:
            base_to_link1 = base_to_link1 + 0.02
        if -1.57 <= link1_to_link2 <= 1.57:
            link1_to_link2 = link1_to_link2 + 0.01
        if -1.57 <= link2_to_dish <= 1.57:
            link2_to_dish = -1 * link1_to_link2
        
        my_pub.publish(robot_state)
        rate_msg.sleep()  
             
if __name__ == '__main__':
    try:
        motion1()
    except rospy.ROSInterruptException:
        pass
