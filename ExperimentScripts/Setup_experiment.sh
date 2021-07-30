#!/bin/sh
#echo  "Mounting Drive";
#sudo mount /dev/sda1 /media/ROS_Storage/
echo  "Starting roscore";
tmux  new-session -d -s  roscore 'roscore' &


printf "Starting canbus set up";
sudo ip link set can0 type can bitrate 500000 listen-only on &
sleep 1
sudo ip link set can0 up &
sleep 2;


echo "Starting main launch file";
tmux  new-session -d -s sensornode 'roslaunch vroom_localization hdl_graph_slam.launch'
sleep 5
echo " "
echo " "
echo "All Tmux sessions should be running.";
echo "  "
tmux ls
