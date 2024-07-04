 #include "ros/ros.h"
#include <gazebo_msgs/SetModelState.h>
#include <cstdlib>
//I'm going to implement user-specified twist values later.
int main (int argc, char **argv)
{
  ros::init(argc,argv,"gazebo_commander");
  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<gazebo_msgs::SetModelState>("/gazebo/set_model_state");
  gazebo_msgs::SetModelState setmodelstate;
  gazebo_msgs::ModelState modelstate;
  modelstate.model_name = "servicer_camera";
  modelstate.reference_frame = "world";

  geometry_msgs::Twist model_twist;
  model_twist.linear.x = 0.5;
  model_twist.linear.y = 0.5;
  model_twist.linear.z = 0.0;
  model_twist.angular.x = 0.25;
  model_twist.angular.y = 0.0;
  model_twist.angular.z = 0.0;
  modelstate.twist = model_twist;

  setmodelstate.request.model_state = modelstate;

  if (client.call(setmodelstate))
  {
    ROS_INFO("Sending");
    ROS_INFO_STREAM(model_twist);
    ROS_INFO("%f, %f",modelstate.pose.position.x,modelstate.pose.position.y);
  }  
  else
  {
    ROS_ERROR("Failed to call service ");
    return 1;
  }
  return 0;  
}
