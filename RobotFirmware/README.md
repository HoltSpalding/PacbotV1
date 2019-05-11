# Robot Firmware

This is the firmware used on Pacbot V1. 

pacbot_ros_pkgs contains all the ros packages run on Pacbot V1. 

To use teleoperate Pacbot, run the following. 

	roslaunch trin_base trin_base.launch
	rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/trin_base_controller/cmd_vel


game_server contains a modified version of Harvard's game engine code that allowed pacbot to connect to the game server and publish gamestate information to other ROS nodes. 

