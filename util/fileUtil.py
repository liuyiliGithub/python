#!/user/bin/env python
#coding:UTF-8

import os

class fileUtil():

	def __init__(self):
		self.basePath = "/data4/question"
		pass

	def createDir(self,path):
		if os.path.exists(path) == False:
			os.makedirs(path)
		else:
			print("该路径已存在")
		pass

	##
	def savePage(self,path,fileName,content):
		filePath = self.basePath+path
		self.createDir(filePath)
		file = open(filePath+"/"+fileName,"w")
		file.write(content)

