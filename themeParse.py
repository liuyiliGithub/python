#!/user/bin/env python
#coding:UTF-8

from bs4 import BeautifulSoup
import imp
myHttpUtil=imp.load_source("myHttpUtil","util/myHttpUtil.py")
from myHttpUtil import down
from questionParse import questionParse

class themeParse():

	def __init__(self):
		self.pc=1
		self.p=1
		self.httpUtil=down()
		self.htmlValue=""
		self.pageCount=0
		self.totalCount=0
		pass

	def getUrl(self,pc,p):
		return "http://www.jyeoo.com/math/report/search?pa=1&pb=0&pc="+str(pc)+"&po=3&pd=1&p="+str(p)

	def execute(self,pc):
		count = self.getPaperList(pc)
		return count


	def getHtml(self,pc,p):
		url = self.getUrl(pc,p)
		self.htmlValue = self.httpUtil.get(url)
		pass

	def getPaperList(self,pc):
		pageCount = self.getPageCount(pc)
		if pageCount == None:
			pCount = self.getPaperDetail(pc,1)
			return pCount
		else:
			count = 0
			for p in range(int(pageCount)):
				pCount = self.getPaperDetail(pc,p+1)
				count = count + pCount
			return count

	def getPaperDetail(self,pc,p):
		self.getHtml(pc,p)
		soup = BeautifulSoup(self.htmlValue,"lxml")
		table = soup.find("table",class_="report-tab")
		count = 0
		totalCount = 0
		if table!=None:
			trs = table.find_all("tr")
			for tr in trs:
				a = tr.find("a",class_="rtitle fleft")
				questionParse().execute(a["href"])
				count += 1
		return count

	#获取当前页数
	def getPageCount(self,pc):
		self.getHtml(pc,1)
		soup = BeautifulSoup(self.htmlValue,"lxml")
		countPage = soup.find("div",class_="page rpage fright")
		if countPage != None:
			for a in countPage.find_all("a"):
				if a.string == u"尾页":
					return a["href"][-2:]

