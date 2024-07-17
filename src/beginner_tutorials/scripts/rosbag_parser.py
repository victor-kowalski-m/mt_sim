import rosbag
from gazebo_msgs.msg import ModelStates
from rospy import Time
from scipy.spatial.transform import Rotation as R
from quat_to_rotvec import to_rotvec


def parse_rosbag(input, output):
    with open(output, "w") as parsed:
        bag = rosbag.Bag(input)
        for topic, msg, t in bag.read_messages():
            msg: ModelStates
            t: Time
            pose = [
                t.to_sec(),
                msg.pose[0].position.x,
                msg.pose[0].position.y,
                msg.pose[0].position.z,
                msg.pose[0].orientation.x,
                msg.pose[0].orientation.y,
                msg.pose[0].orientation.z,
                msg.pose[0].orientation.w
            ]
            parsed.write(" ".join([f"{i:.4f}" for i in pose])+"\n")
        bag.close()

in_real_traj_bag = '/home/victor/maps/rrt_ur_32/2024-07-17-11-18-13.bag'
out_real_traj_txt = '/home/victor/maps/rrt_ur_32/2024-07-17-11-18-13.txt'

parse_rosbag(in_real_traj_bag, out_real_traj_txt)
to_rotvec(out_real_traj_txt, out_real_traj_txt)

in_cam_traj_txt = '/home/victor/maps/rrt_ur_32/CamTraj.txt'
out_cam_traj_txt = '/home/victor/maps/rrt_ur_32/CamTraj_rotvec.txt'
to_rotvec(in_cam_traj_txt, out_cam_traj_txt)

in_key_traj_txt = '/home/victor/maps/rrt_ur_32/KeyFrameTrajectory.txt'
out_key_traj_txt = '/home/victor/maps/rrt_ur_32/KeyFrameTrajectory_rotvec.txt'
to_rotvec(in_key_traj_txt, out_key_traj_txt)
