#!/user/bin/env python
#coding:UTF-8

from bs4 import BeautifulSoup
import imp
myHttpUtil=imp.load_source("myHttpUtil","util/myHttpUtil.py")
from myHttpUtil import down

class searchParse():

	def __init__(self):
		self.url="http://www.jyeoo.com/search?p=1&c=1&qb=%e5%ae%89%e5%be%bd&s=20&t=0"
		pass

	def execute(self):
		self.getHtml()
		pass

	def getHtml(self):
		html = open("test2.html","r").read()
		soup = BeautifulSoup(html,"lxml")
		div = soup.find("fieldset").find("div",class_="pt1")
		div.find("div",class_="quizPutTag").extract()
		div.find("div",class_="sanwser").extract()
		print(div)
		pass


searchParse().execute()