#!/usr/bin/env python
import rospy

import math
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import Pose

if __name__ == '__main__':
    rospy.init_node('tf2_forward')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)


    rate = rospy.Rate(60.0)
    pose_pub = rospy.Publisher("fusedPose", Pose, queue_size=5)
    pose = Pose()

    #pose.child_frame_id = "vr_link"

    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform('map', 'base_link', rospy.Time())
            
            pose.position = trans.transform.translation;
            pose.orientation = trans.transform.rotation;
            pose_pub.publish(pose   )


        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        rate.sleep()
