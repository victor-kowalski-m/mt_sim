#!/usr/bin/env python

from __future__ import print_function

from gazebo_msgs.srv import ApplyBodyWrench, ApplyBodyWrenchRequest
import rospy
import numpy as np
import sys

if __name__ == "__main__":
    apply_wrench = rospy.ServiceProxy("/gazebo/apply_body_wrench", ApplyBodyWrench)
    abw = ApplyBodyWrenchRequest()
    abw.body_name = "robot::com"
    abw.reference_frame = "robot::com"
    abw.wrench.force.y = -1
    abw.duration.secs = 3
    resp = apply_wrench(abw)

    print(abw)
    print(resp)

    