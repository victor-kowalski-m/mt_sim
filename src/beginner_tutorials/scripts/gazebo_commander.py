#!/usr/bin/env python

from __future__ import print_function

from gazebo_msgs.srv import SetModelState, SetModelStateRequest
import rospy
import numpy as np
import sys

if __name__ == "__main__":
    set_model = rospy.ServiceProxy("/gazebo/set_model_state", SetModelState)
    sms = SetModelStateRequest()
    sms.model_state.model_name = "robot"
    sms.model_state.pose.position.x = -2
    sms.model_state.pose.position.z = 0.8
    sms.model_state.pose.orientation.x = 0
    sms.model_state.pose.orientation.y = 0
    sms.model_state.pose.orientation.z = 0.70710678
    sms.model_state.pose.orientation.w = 0.70710678

    # sms.model_state.twist.linear.x = 0.35
    # sms.model_state.twist.angular.y = 0.1
    # resp = set_model(sms)
    # while True:
    #     pass

    # while True:
    #     rospy.sleep(0.01)
    #     resp = set_model(sms)
    #     print("x:", sms.model_state.twist.linear.x , "\n", resp)
    #     sms.model_state.twist.linear.x  += 0.004
    #     if sms.model_state.twist.linear.x >= 2:
    #         break  
    # resp = set_model(sms)
    # sys.exit()

    while True:
        rospy.sleep(0.01)
        resp = set_model(sms)
        print("z:", sms.model_state.pose.position.z, "\n", resp)
        sms.model_state.pose.position.z += 0.004
        if sms.model_state.pose.position.z>= 1.2:
            break     
    while True:
        rospy.sleep(0.01)
        resp = set_model(sms)
        print("x:", sms.model_state.pose.position.x, "\n", resp)
        sms.model_state.pose.position.x += 0.004
        if sms.model_state.pose.position.x>= 2:
            break   
    while True:
        rospy.sleep(0.01)
        resp = set_model(sms)
        print("z:", sms.model_state.pose.position.z, "\n", resp)
        sms.model_state.pose.position.z -= 0.004
        if sms.model_state.pose.position.z<= 0.8:
            break     
    while True:
        rospy.sleep(0.01)
        resp = set_model(sms)
        print("x:", sms.model_state.pose.position.x, "\n", resp)
        sms.model_state.pose.position.x -= 0.004
        if sms.model_state.pose.position.x<= -2:
            break  

    # z_start = sms.model_state.pose.position.z 
    # z_ang = 0
    # while True:
    #     rospy.sleep(0.01)
    #     resp = set_model(sms)
    #     print("x:", sms.model_state.pose.position.x, "\n", resp)
    #     sms.model_state.pose.position.x += 0.004
    #     z_ang += 0.01
    #     sms.model_state.pose.position.z = z_start+0.2*np.sin(z_ang)
    #     if sms.model_state.pose.position.x >= 0:
    #         break
    # while True:
    #     rospy.sleep(0.01)
    #     resp = set_model(sms)
    #     print("y:", sms.model_state.pose.position.y, "\n", resp)
    #     sms.model_state.pose.position.y += 0.004
    #     if sms.model_state.pose.position.y >= 1:
    #         break

    # sms.model_state.pose.position.y = 0
    # sms.model_state.pose.position.z = 0

    # sms.model_state.twist.linear.x = 0.2
    # sms.model_state.twist.linear.z = 0.2


