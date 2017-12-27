#!/user/bin/env python
#coding:UTF-8

from bs4 import BeautifulSoup
import imp
myHttpUtil=imp.load_source("myHttpUtil","util/myHttpUtil.py")
mongoUtil=imp.load_source("mongoUtil","util/mongoUtil.py")
idUtil=imp.load_source("idUtil","util/idUtil.py")
fileUtil=imp.load_source("fileUtil","util/fileUtil.py")
from fileUtil import fileUtil
from myHttpUtil import down
from mongoUtil import mongoUtil
from questionDetail import questionDetail
from idUtil import idUtil

class questionParse():

	def __init__(self):
		self.httpUtil=down()
		self.htmlValue=""
		self.paperName=""
		self.questionList=[]
		self.idUtil=idUtil()
		self.mongoUtil=mongoUtil("kpdata")
		self.fileUtil = fileUtil()
		pass

	def execute(self,url):
		self.getHtml(url)
		self.getQuestionList()
		pass

	def getHtml(self,url):
		self.htmlValue = self.httpUtil.get(url)
		pass

	def getQuestionList(self):
		soup = BeautifulSoup(self.htmlValue,"lxml")
		div = soup.find("div",class_="rpt-bg")
		if div == None:
			return
		rpt_h = div.find("div",class_="rpt_h")
		if rpt_h == None:
			return
		rpt_count = rpt_h.find("div",class_="rpt-count")
		self.paperName = rpt_h.find("h1").string
		fields = div.find("div",class_="rpt_b").find_all("fieldset")
		paper = {}
		paper["sourceNotes"]=self.paperName
		paper["year"]=self.getPaperYear(self.paperName)
		if rpt_count!=None:
			score = rpt_count.strings.next()[3:]
			if score!=None:
				paper["score"]=int(score)
		paperId = self.idUtil.getUUID()
		paper["_id"]=paperId
		paper["dr"]=0
		self.savePaperHtml(self.paperName)
		paperIdList = []
		paperIdList.append(paperId)
		self.savePaper(paper)
		# print(self.paperName)
		h3List = div.find("div",class_="rpt_b").find_all("h3")
		for index,h3 in enumerate(h3List):
			fs = h3.next_sibling.find_all("fieldset")
			self.questionWithType(fs,(index+1)*100,paperIdList)
		pass

	def questionWithType(self,fields,questionType,paperIdList):
		questionList=[]
		for f in fields:
			idStr = f["id"]
			pt1 = f.find("div",class_="pt1")
			if pt1 != None:
				qseq = pt1.find("span",class_="qseq")
				if qseq != None:
					index = "".join(qseq.string)
					question = questionDetail().execute(idStr,questionType,self.paperName,index)
					if question!=None:
						question["paperIdList"]=paperIdList
						questionList.append(question)
		self.saveQuestionList(questionList)
		pass

	def savePaperHtml(self,paperName):
		# self.fileUtil.savePage("/"+paperName,"paper.html",self.htmlValue)
		pass

	def getPaperYear(self,str1):
		str1 = "".join(str1)
		try:
			xn = str1.index(u"学年")
			year = int(str1[n-4:n])
			return year
		except Exception as e:
			try:
				n = str1.index(u"年")
				year = int(str1[n-4:n])
				return year
			except Exception as e:
				print("该试卷无年份")
			pass


	def saveQuestionList(self,questionList):
		self.mongoUtil.insert(questionList,"NormalQuestion")
		pass

	def savePaper(self,paper):
		self.mongoUtil.insert(paper,"Paper")
		pass

	def test(self):
		self.execute("http://www.jyeoo.com/math/report/detail/f906b3d8-0fd3-41dc-98d9-40b24d8700e0")
		pass