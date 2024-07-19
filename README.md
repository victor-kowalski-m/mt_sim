Terminals

1. `roscore`
2. `rosrun gazebo_ros gazebo gazebo/oos_cam.world`
3. `rviz` (in the gui, open rviz/cam_view.rviz)
4. `rosrun topic_tools throttle messages /gazebo/model_states 30`
5. `rosbag record gazebo/model_states_throttle`
6. `rosrun ORB_SLAM3 Mono Vocabulary/ORBvoc.txt Examples/Monocular/my_cam.yaml`
7. `rosrun beginner_tutorials traj_commander.py`




