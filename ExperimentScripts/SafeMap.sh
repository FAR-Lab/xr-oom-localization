#!/bin/sh
#echo  "Whats the Parrticipant ID? (Full ID) (e.g. NYC-01)";
read -p "Whats the Parrticipant ID? (Full ID) (e.g. NYC-01)" ParticipantID
read -p "Whats the condition? 1 or 2 or 3" Condition
echo "  "
echo "Starting recording!"



rosservice call ../../../hdl_graph_slam/save_map "resolution: 0.05 destination: '/home/carlab/recordings/${ParticipantID}_C${Condition}_map.pcd'"
#rosbag record -o "/home/carlab/recordings/${ParticipantID}_C${Condition}"  -b 2048 /os1_cloud_node/points /os1_cloud_node/imu /odomCAN /imu/mag /imu/data
#rosbag record -o "/media/farlab/Samsung_T5/recordings/${ParticipantID}_C${Condition}" -a -b 2048 -x"/os1_node/(.*)"
