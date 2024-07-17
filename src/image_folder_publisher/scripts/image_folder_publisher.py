#!/usr/bin/env python3
from __future__ import print_function

import roslib
roslib.load_manifest('image_folder_publisher')

import sys
import os
from os import listdir
from os.path import isfile, join
import datetime
import rospy
import cv2

from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError

class image_folder_publisher:
    def __init__(self):
        self.__app_name = "image_folder_publisher"
        self.w = 528
        self.h = 406
        self.f = 684

        self._cv_bridge = CvBridge()

        self._topic_name = rospy.get_param('~topic_name', '/image_raw')
        rospy.loginfo("[%s] (topic_name) Publishing Images to topic  %s", self.__app_name, self._topic_name)

        self._image_publisher = rospy.Publisher(self._topic_name, Image, queue_size=1)
        # self._info_publisher = rospy.Publisher("/camera/camera_info", CameraInfo, queue_size=1)

        self._rate = rospy.get_param('~publish_rate', 30)
        rospy.loginfo("[%s] (publish_rate) Publish rate set to %s hz", self.__app_name, self._rate)

        self._sort_files = rospy.get_param('~sort_files', True)
        rospy.loginfo("[%s] (sort_files) Sort Files: %r", self.__app_name, self._sort_files)

        self._frame_id = rospy.get_param('~frame_id', 'camera')
        rospy.loginfo("[%s] (frame_id) Frame ID set to  %s", self.__app_name, self._frame_id)

        self._loop = rospy.get_param('~loop', 1)
        rospy.loginfo("[%s] (loop) Loop  %d time(s) (set it -1 for infinite)", self.__app_name, self._loop)

        self._image_folder = rospy.get_param('~image_folder', '')

        self._sleep = rospy.get_param('~sleep', 0.0)
        rospy.sleep(self._sleep)
        rospy.loginfo("[%s] (sleep) Sleep %f seconds after each image", self.__app_name, self._sleep)
        
        if self._image_folder == '' or not os.path.exists(self._image_folder) or not os.path.isdir(self._image_folder):
            rospy.logfatal("[%s] (image_folder) Invalid Image folder", self.__app_name)
            sys.exit(0)
        rospy.loginfo("[%s] Reading images from %s", self.__app_name, self._image_folder)

    def run(self):
        ros_rate = rospy.Rate(self._rate)

        files_in_dir = [f for f in listdir(self._image_folder) if isfile(join(self._image_folder, f))]
        for f in files_in_dir:
            splitted = f.split(".")
            if len(splitted) == 3:
                os.rename(join(self._image_folder, f), join(self._image_folder, splitted[0]+splitted[1]+"."+splitted[2]))
        files_in_dir = [f for f in listdir(self._image_folder) if isfile(join(self._image_folder, f))]
        if self._sort_files:
            files_in_dir.sort()
        try:
            while self._loop != 0:
                for f in files_in_dir:
                    if not rospy.is_shutdown():
                        if isfile(join(self._image_folder, f)):
                            cv_image = cv2.imread(join(self._image_folder, f))
                            if cv_image is not None:
                                ros_msg = self._cv_bridge.cv2_to_imgmsg(cv_image, "bgr8")
                                ros_msg.header.frame_id = self._frame_id
                                pic_name = f.split(".")[0]

                                ros_msg.header.stamp = rospy.Time(nsecs=int(pic_name)*10**(19-len(pic_name)))
                                self._image_publisher.publish(ros_msg)
                                info_msg = CameraInfo()
                                info_msg.header.frame_id = self._frame_id
                                info_msg.header.stamp = ros_msg.header.stamp
                                info_msg.width = self.w
                                info_msg.height = self.h
                                # info_msg.distortion_model = "plumb_bob"
                                # info_msg.D = [0]*5
                                # info_msg.K = [

                                # self._info_publisher.publish(info_msg)
                                rospy.loginfo("[%s] Published %s", self.__app_name, join(self._image_folder, f))
                                rospy.loginfo(f"Timestamp: {ros_msg.header.stamp}")
                                rospy.loginfo(f"Datetime: {datetime.datetime.fromtimestamp(ros_msg.header.stamp.secs)}")
                            else:
                                rospy.loginfo("[%s] Invalid image file %s", self.__app_name, join(self._image_folder, f))
                            ros_rate.sleep()
                    else:
                        return
                self._loop = self._loop - 1
        except CvBridgeError as e:
            rospy.logerr(e)


def main(args):
    rospy.init_node('image_folder_publisher', anonymous=True)

    image_publisher = image_folder_publisher()
    image_publisher.run()


if __name__ == '__main__':
    main(sys.argv)