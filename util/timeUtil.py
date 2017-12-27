#!/usr/bin/env python
#coding: UTF-8

import time


class timeUtil():

	def __init__(self):
		pass

	def getLocalTimeMill(self):
		return long(time.time()*1000)

	def getStartTime(self,text):
		return text[0:-8]

	def getEndTime(self,text):
		return text[0:10]+text[-6:]

	def getTimeMill(self,text):
		return text[6:-7]