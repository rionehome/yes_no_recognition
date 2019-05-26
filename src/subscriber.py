#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String,Bool

def callback(message):
	print(message.data)
	pub.publish(True)

if __name__ == '__main__':
	rospy.init_node('subscriber', anonymous=True)
	rospy.Subscriber('recognition_result', String, callback) # 音声認識結果
	pub = rospy.Publisher('recognition_start', Bool, queue_size=10) # 音声認識開始の合図
	rospy.spin()
