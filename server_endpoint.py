#!/usr/bin/env python

import rospy

from tcp_endpoint.RosTCPServer import TCPServer
from tcp_endpoint.RosPublisher import RosPublisher
from tcp_endpoint.RosSubscriber import RosSubscriber
from tcp_endpoint.RosService import RosService

from geometry_msgs.msg import PoseStamped

def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 1024)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TCPServer(ros_node_name, buffer_size, connections)

    tcp_server.source_destination_dict = {
        'pose': RosSubscriber('/zedm/zed_node/pose', PoseStamped, tcp_server)
    }
    #'pose': RosSubscriber('/zedm/zed_node/pose', Pose, tcp_server)

    rospy.init_node(ros_node_name, anonymous=True)
    tcp_server.start()
    rospy.spin()


if __name__ == "__main__":
    main()
