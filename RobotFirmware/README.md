

source devel/setup.bash
roslaunch trin_base trin_base.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py cmd_vel:=/trin_base_controller/cmd_vel

