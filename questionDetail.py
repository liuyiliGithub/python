#!/user/bin/env python
#coding:UTF-8

import bs4
import imp
myHttpUtil=imp.load_source("myHttpUtil","util/myHttpUtil.py")
idUtil=imp.load_source("idUtil","util/idUtil.py")
mongoUtil=imp.load_source("mongoUtil","util/mongoUtil.py")
fileUtil=imp.load_source("fileUtil","util/fileUtil.py")
from fileUtil import fileUtil
from idUtil import idUtil
from myHttpUtil import down


class questionDetail():

	def __init__(self):
		self.htmlValue = ""
		self.urlPre = "http://www.jyeoo.com/math/ques/detail/"
		self.choiceClass="com.kpdata.core.entity.question.NormalChoiceQuestion"
		self.zgClass="com.kpdata.core.entity.question.NormalZGQuestion"
		self.tkClass="com.kpdata.core.entity.question.NormalTKQuestion"
		self.htmlUtil = down()
		self.idUtil = idUtil()
		self.fileUtil = fileUtil()
		pass

	def execute(self,idStr,questionType,paperName,index):
		return self.getHtmlAndParse(questionType,idStr,paperName,index)

	def getHtmlAndParse(self,questionType,idStr,paperName,index):
		self.getHtml(idStr,paperName,index)
		soup = bs4.BeautifulSoup(self.htmlValue,"lxml")
		div = soup.find("div",class_="ques-detail")
		if div == None:
			return
		qtBody = div.find("fieldset",id=idStr)
		if qtBody != None:
			qdetail = {}
			qdetail["_id"]=self.idUtil.getUUID()
			qdetail["type"]=questionType
			#题目
			qHeadSoup = qtBody.find("div",class_="pt1")
			if qHeadSoup != None:
				qdetail["content"]=qContent
				sanwser = qHeadSoup.find_all("div",class_="sanwser")
				if sanwser!=None:
					##将填空题中的答案去掉
					qHeadSoup.find("div",class_="quizPutTag").extract()
					qHeadSoup.find("div",class_="sanwser").extract()
					directAnswer=[]
					for anwser in sanwser:
						directAnswer.append(anwser.string)
					qdetail["directAnswer"]=directAnswer
					self.printOne(directAnswer)
				qContent = ""
				for s in qHeadSoup.strings:
					qContent = qContent+s
				self.printOne(qContent)
			#选项
			qOptionSoup = qtBody.find("div",class_="pt2")
			if qOptionSoup!=None:
				ss = qOptionSoup.find_all("label",class_=" s")
				directAnswer = []
				if ss != None:
					answerCount = 0
					for s in ss:
						answer = s.strings.next()[0:1]
						directAnswer.append(answer)
						answerCount+=1
					qdetail["choiceType"]=answerCount
					qdetail["directAnswer"]=directAnswer
					self.printOne(directAnswer)
				qdetail["options"]=qOptionSoup.prettify()
				self.printOne(qOptionSoup.prettify())
			if questionType == 100:
				qdetail["_class"]=self.choiceClass
			elif questionType == 200:
				qdetail["_class"]=self.tkClass
			elif questionType == 300:
				qdetail["_class"]=self.zgClass
			#考点
			qKpointSoup = qtBody.find("div",class_="pt3")
			if qKpointSoup != None:
				qKpoint = []
				for aTag in qKpointSoup.find_all("a"):
					if aTag != None:
						qKpoint.append(aTag.string)
				qdetail["kpoint"]=qKpoint
				self.printOne(qKpoint)
			#分析
			qAnalysisSoup = qtBody.find("div",class_="pt5")
			if qAnalysisSoup != None:
				qAnalysis = ""
				for s in qAnalysisSoup.strings:
					qAnalysis = qAnalysis+s
				qdetail["analysis"]=qAnalysis
				self.printOne(qAnalysis)
			#解答
			qAnwserSoup = qtBody.find("div",class_="pt6")
			if qAnwserSoup != None:
				qAnwser = ""
				for s in qAnwserSoup.strings:
					qAnwser = qAnwser+s
				qdetail["anwser"]=qAnwser
				self.printOne(qAnwser)
			#点评
			qCommentSoup = qtBody.find("div",class_="pt7")
			if qCommentSoup != None:
				qComment = ""
				for s in qCommentSoup.strings:
					qComment = qComment+s
				qdetail["comment"]=qComment
				self.printOne(qComment)

			#题目详情
			fieldtip = div.find("span",class_="fieldtip")
			if fieldtip != None:
				difficulty = fieldtip.find("label").find("em").string
				qdetail["difficulty"] = difficulty
				self.printOne(difficulty)
			qdetail["dr"]=0
		return qdetail

	def printOne(self,one):
		# print(one)
		pass

	def getHtml(self,idStr,paperName,index):
		self.htmlValue = self.htmlUtil.get(self.urlPre+idStr)
		# fileName = index+".html"
		# self.fileUtil.savePage("/"+paperName+"/ques",fileName,self.htmlValue)
		pass
