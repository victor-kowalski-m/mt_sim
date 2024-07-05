Terminals

1. `roscore`
2. `rosrun gazebo_ros gazebo gazebo/oos_cam.world` (adjust viewing angle)
3. `rviz` (open rviz/cam_view.rviz)
4. `rosrun topic_tools throttle messages /gazebo/model_states 30`
5. `rosbag record /camera/image_raw /gazebo/model_states_throttle`
6. `rosrun beginner_tutorials gazebo_commander.py`

When 6 is over, kill 5. Then run:

`$ASTROBEE_BUILD_PATH/devel/lib/localization_node/extract_image_bag <bag.bag> -use_timestamp_as_image_name -image_topic /camera/image_raw -output_directory <folder>`
