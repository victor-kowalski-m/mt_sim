#!/usr/bin/env python

from __future__ import print_function

from gazebo_msgs.srv import SetModelState, SetModelStateRequest
from sensor_msgs.msg import Imu
import rospy
import numpy as np
import sys
from scipy.spatial.transform import Rotation as R

def traj_commander():
    freq = 100
    
    traj = np.load("/home/victor/catkin_ws/data/trajs_to_command/parsed/rrt_ur_32.npy")

    # duration = 40
    # n_points = freq*duration

    # quat = R.from_rotvec([0, 0, 0*np.pi/2]).as_quat().tolist()
    # quat = R.from_rotvec([0, 0, np.pi]).as_quat().tolist()
    # print(quat)
    # quat = R.from_rotvec([0, 0, -np.pi]).as_quat().tolist()
    # print(quat)
    # sys.exit()

    # traj = []
    # x_points = np.linspace(-2.5, 1.5, n_points)
    # for i in range(n_points):
    #     traj.append([x_points[i], 0, 1.4]+[0, 0, 0, 0])
    

    set_model = rospy.ServiceProxy("/gazebo/set_model_state", SetModelState)
    sms = SetModelStateRequest()
    sms.model_state.model_name = "robot"

    # pub = rospy.Publisher('imu', Imu, queue_size=10)
    # imu = Imu()

    rospy.init_node('traj_commander', anonymous=True)
    rate = rospy.Rate(freq) # 100hz

    state = traj[0]
    sms.model_state.pose.position.x = state[0]
    sms.model_state.pose.position.y = state[1]
    sms.model_state.pose.position.z = state[2]
    sms.model_state.pose.orientation.x = state[3]
    sms.model_state.pose.orientation.y = state[4]
    sms.model_state.pose.orientation.z = state[5]
    sms.model_state.pose.orientation.w = state[6]                                       
    resp = set_model(sms)
    rospy.sleep(3)

    for state in traj:
        # print("z:", sms.model_state.pose.position.z, "\n", resp)
        sms.model_state.pose.position.x = state[0]
        sms.model_state.pose.position.y = state[1]
        sms.model_state.pose.position.z = state[2]
        sms.model_state.pose.orientation.x = state[3]
        sms.model_state.pose.orientation.y = state[4]
        sms.model_state.pose.orientation.z = state[5]
        sms.model_state.pose.orientation.w = state[6]

        # imu.header.stamp = rospy.Time.now()
        # imu.orientation = sms.model_state.pose.orientation
        # imu.angular_velocity.x = state[10]
        # imu.angular_velocity.y = state[11]
        # imu.angular_velocity.z = state[12]
        # imu.linear_acceleration.x = state[13]
        # imu.linear_acceleration.y = state[14]
        # imu.linear_acceleration.z = state[15]
                                       
        resp = set_model(sms)
        # pub.publish(imu)

        rate.sleep()
   
if __name__ == '__main__':
    try:
        traj_commander()
    except rospy.ROSInterruptException:
        pass