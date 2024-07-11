import rosbag
from gazebo_msgs.msg import ModelStates
from rospy import Time
from scipy.spatial.transform import Rotation as R
from quat_to_rotvec import to_rotvec

in_cam_traj_txt = '/home/victor/maps/astrobee going forward/CamTraj.txt'
out_cam_traj_txt ='/home/victor/maps/astrobee going forward/CamTraj_rotvec.txt'
to_rotvec(in_cam_traj_txt, out_cam_traj_txt)

in_key_traj_txt = '/home/victor/maps/astrobee going forward/KeyFrameTrajectory.txt'
out_key_traj_txt = '/home/victor/maps/astrobee going forward/KeyFrameTrajectory_rotvec.txt'
to_rotvec(in_key_traj_txt, out_key_traj_txt)
