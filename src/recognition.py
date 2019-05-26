#!/usr/bin/env python
# -*- coding: utf-8 -*-
# PocketSphinx 音声認識

import rospy
from std_msgs.msg import String, Bool
import os
from pocketsphinx import LiveSpeech

class Recognition:
	def recognition(self):
		while 1:
			if self.speech_recognition == True:
				self.resume()
				self.speech_recognition = False # 音声認識停止
			elif self.speech_recognition == False:
				self.pause()
				while self.speech_recognition != True:
					pass
	# 音声認識
	def resume(self):
		print('== START RECOGNITION ==')
		speech = LiveSpeech(
		verbose=False, sampling_rate=8000, buffer_size=2048, no_search=False, full_utt=False,
		hmm=os.path.join(self.model_path, 'en-us'),
		lm=os.path.join(self.model_path, 'en-us.lm.bin'),
		dic=os.path.join(self.dictionary_path, 'yes_no_sphinx.dict')
		)
		for text in speech:
			text = str(text)
			self.pub.publish(text) # 音声認識の結果をpublish
			break
# 音声認識ストップ
	def pause(self):
		print('== STOP RECOGNITION ==')
		speech = LiveSpeech(
		verbose=False, sampling_rate=8000, buffer_size=2048, no_search=True, full_utt=False,
		hmm=os.path.join(self.model_path, 'en-us'),
		lm=os.path.join(self.model_path, 'en-us.lm.bin'),
		dic=os.path.join(self.dictionary_path, 'yes_no_sphinx.dict')
		)

	# 音声認識開始のメッセージを受け取る
	def control(self, data):
		self.speech_recognition = data.data


	def __init__(self):
		rospy.init_node('recognition', anonymous=True)
		rospy.Subscriber('recognition_start', Bool, self.control) # 音声認識開始の合図
		self.pub = rospy.Publisher('recognition_result', String, queue_size=10) # 音声認識結果
		# 絶対パス
		self.model_path = '/usr/local/lib/python2.7/dist-packages/pocketsphinx/model' # 音響モデル
		self.dictionary_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dictionary') # 辞書

		self.speech_recognition = False # 音声認識のスタートとストップ
		self.recognition()


if __name__ == '__main__':
	Recognition()