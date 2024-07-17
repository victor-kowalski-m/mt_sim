Terminals

1. `roscore`
2. `rosrun gazebo_ros gazebo gazebo/oos_cam.world` (adjust viewing angle)
3. `rviz` (open rviz/cam_view.rviz)
4. `rosrun topic_tools throttle messages /gazebo/model_states 30`
5. `rosbag record /camera/image_raw /gazebo/model_states_throttle`
6. `rosrun beginner_tutorials gazebo_commander.py`

When 6 is over, kill 5. Then run:

`$ASTROBEE_BUILD_PATH/devel/lib/localization_node/extract_image_bag <bag.bag> -use_timestamp_as_image_name -image_topic /camera/image_raw -output_directory <folder>`

OR, with SLAM ROS:
1. `roscore`
2. `rosrun gazebo_ros gazebo gazebo/oos_cam.world` (adjust viewing angle)
3. `rviz` (open rviz/cam_view.rviz)
4. `rosrun topic_tools throttle messages /gazebo/model_states 30`
5. `rosbag record gazebo/model_states_throttle`
6. `rosrun ORB_SLAM3 Mono Vocabulary/ORBvoc.txt Examples/Monocular/my_cam.yaml` (in ORB_SLAM3/ possibly delete CamFrames.txt, Keypoints*.txt, *Map.txt. Run ./build.sh and ./build_ros.sh)
7. `rosrun beginner_tutorials gazebo_commander.py`

Do CTRL-C in terminal 6.

rosrun ORB_SLAM3 Mono_Inertial Vocabulary/ORBvoc.txt /home/victor/ORB_SLAM3/Examples/Monocular-Inertial/my_cam.yaml true	

C++:
1. test_optimizer
2. gen_traj_to_slam_opt

Drive

Ubuntu/ROS/SLAM
1. bspline_parser.py
2. create dir in maps
3. record rosbag in it
4. traj_commander + all mapping steps....  / video recording
5. copy slam files to created dir in maps
6. rosbag_parser.py
7. copy video to dir in maps

Drive

MATLAB

1. Copy 2 of test_sim_map ?

Tomorrow: get traj w10 -3.13

Let RRT*-GBO run, collect some solutions.
- w09




