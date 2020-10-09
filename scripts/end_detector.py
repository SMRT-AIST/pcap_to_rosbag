#!/usr/bin/python
import rospy
from velodyne_msgs.msg import *


def main():
	rospy.init_node('end_detector')

	last_received = rospy.Time.now()
	def scan_callback(msg):
		nonlocal last_received
		last_received = rospy.Time.now()
	sub = rospy.Subscriber('/velodyne_packets', VelodyneScan, scan_callback)

	def timer_callback(event):
		since_last_msg = rospy.Time.now() - last_received
		print('since_last_msg: %.3f[sec]' % since_last_msg.to_sec())
		if since_last_msg > rospy.Duration(5.0):
			rospy.signal_shutdown('velodyne packets have been terminated')

	timer = rospy.Timer(rospy.Duration(1.0), timer_callback)

	rospy.spin()


if __name__ == '__main__':
	main()
