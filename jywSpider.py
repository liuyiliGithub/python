#!/user/bin/env python
#coding:UTF-8

#按照试卷层面爬数据

from bs4 import BeautifulSoup
import imp
myHttpUtil=imp.load_source("myHttpUtil","util/myHttpUtil.py")
from myHttpUtil import down
from themeParse import themeParse
from threading import Thread


class jywSpider():
	
	def __init__(self):
		self.urlPre = "http://www.jyeoo.com"
		self.httpUtil=down()
		self.htmlValue=""
		self.themeUrlList = []#主题列表url
		self.totalPaperCount = 0
		pass

	def execute(self):
		self.getExamPaperList()
		self.getThemeUrl()
		pass

	def getExamPaperList(self):
		url = self.urlPre+"/math/report/search"
		self.htmlValue = self.httpUtil.get(url)
		pass

	def getThemeUrl(self):
		soup = BeautifulSoup(self.htmlValue,"lxml")
		div = soup.find("div",class_="paper-box report-tree fleft")
		lis = div.find("ul").find_all("li")
		threads = []
		for li in lis:
			aTag = li.find("a")
			href = aTag["href"]
			name = aTag.string
			pc = int(href[-11:-10])
			if pc < 8:
				t = Thread(target=self.themeExecute,args=(pc,name,))
				threads.append(t)
		for t in threads:
			t.start()
		pass

	def themeExecute(self,pc,name):
		count = themeParse().execute(pc)
		print(name+":"+str(count))
		pass

jywSpider().execute()
# jywSpider().test()