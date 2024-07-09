import rosbag
from gazebo_msgs.msg import ModelStates
from rospy import Time
from scipy.spatial.transform import Rotation as R


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

def to_rotvec(input, output):
    all = []
    with open(input, "r") as f:
        lines = f.readlines()
        for line in lines:
            items = line.split(" ")
            items = [float(i) for i in items if i != ""]
            quat = R.from_quat(items[4:])
            items = items[:4] + quat.as_rotvec().tolist()
            all.append(items)
    with open(output, "w") as f:    
        for state in all:
            f.write(" ".join([f"{i:.4f}" for i in state])+"\n")

in_real_traj_bag = '/home/victor/catkin_ws/data/bags/2024-07-07-20-41-25.bag'
out_real_traj_txt = '/home/victor/catkin_ws/data/resulting_trajs/real2024-07-07-20-41-25.txt'

parse_rosbag(in_real_traj_bag, out_real_traj_txt)
to_rotvec(out_real_traj_txt, out_real_traj_txt)

in_cam_traj_txt = '/home/victor/catkin_ws/data/slam_locs/CamTraj.txt'
out_cam_traj_txt = '/home/victor/catkin_ws/data/resulting_trajs/cam2024-07-07-20-41-25.txt'
to_rotvec(in_cam_traj_txt, out_cam_traj_txt)

in_key_traj_txt = '/home/victor/catkin_ws/data/slam_locs/KeyFrameTrajectory.txt'
out_key_traj_txt = '/home/victor/catkin_ws/data/resulting_trajs/key2024-07-07-20-41-25.txt'
to_rotvec(in_key_traj_txt, out_key_traj_txt)
