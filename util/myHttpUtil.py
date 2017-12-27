#!/usr/bin/env python
#coding: UTF-8

import urllib
import urllib2
import imp
mongoUtil=imp.load_source("mongoUtil","/data4/util/mongoUtil.py")
timeUtil=imp.load_source("timeUtil","/data4/util/timeUtil.py")
from mongoUtil import mongoUtil
from timeUtil import timeUtil

class down():

	def __init__(self):
		self.dbUtil = mongoUtil("kpdata")
		self.timeUtil = timeUtil()
		pass

	def get(self,url):
		headers = self.getHeaders()
		request = urllib2.Request(url,headers = headers)
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		response = opener.open(request)
		html = response.read().replace("charset=gb2312","")
		# self.dbUtil.insert({"html":html,"time":self.timeUtil.getLocalTimeMill()},"requestHtml")
		return html

	def getWithProxy(self,url):
		headers = self.getHeaders()
		request = urllib2.Request(url,headers = headers)
		proxy_s = urllib2.ProxyHandler({"http":"222.242.106.142:63000"})
		opener = urllib2.build_opener(proxy_s)
		response = opener.open(request)
		return response.read().replace("charset=gb2312","")
	
	def post(self,url,data):
		request = urllib2.Request(url,headers = self.getHeaders())
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
		enData = urllib.urlencode(data)
		response = opener.open(request,enData)
		return response.read().replace("charset=gb2312","")

	def getHeaders(self):
		#贵宾的账号
		cookie = "jyean=itgm_FxyHHatM64X0V45dFzj-XdKs_PxiDUtC9wjO3G9F59ysi7rwCVhtx0bIIHBvGHl00w_icyKnsg80HsNa7kWqIHJi45fDiXhL-qqwNdlatAEJSndwNZwwxsM2nKK0; UM_distinctid=16053a130f753e-0ab8718eded2a3-163c6654-fa000-16053a130f872; __RequestVerificationToken=5HqfyTwRi14_dwzL6IpYPEohZZ4IgMhGxOlMRUjvAH32WnMpUPgZPDW09Tuw3YIMSjGy3V0RZ-ZMns9EApvkhcCKVevPv22AjyoZ87r0qmw1; jye_search_q=1; jy_user_rg_math=; remind_check=1; CNZZDATA2018550=cnzz_eid%3D1715564386-1513229849-%26ntime%3D1513753852; jy_user_ed_math=16; LF_Email=18513309509; jy=9C2A471A8BE4B96877ADF2547DCD5CADE6BD95941BE069DCCD76089B7107D1E9FC57A0A1457F6CA5D3E19FB30980A2D1F622E7000803EC8963151A0CFAD219CBD18C22FC9F80657F9E960C816AEF8E08A3517477165D71DBEB5DE663291826118D1F047859EAD466A7E570B0582BC5D1743A74B630A94D4FBB6310CCDB0DE0B8D2DBCE185DB21EB0810D3307AA072BAF290EB84A7F23C84C43A2C2B45A97BA2D0FCEA0E4E8870C031CB5F7E7BB3168E9A3F6EA45FA5B3B42C334100BC011DDBC004EB1F4AD203B19F12461E29D23FDE100B3EF2A6D2781E7EDF51756FA91F43264DB99A9498866886A25421A14CBF53A4A9A1AED5C4BBD84EECB2C8A2AB7964FFAD5BB3AE4732946CCE0B5051BBD6F6FDE00A0A57243FAEB0E0FF182C2C0EFE3DF4623EC3E8C43B7C3BA1A468F8D8995184FA88206631EDA9835BFF37BB322ED29B547A72CD0119D95CA983A50C88619; JYERN=0.5999090200937371"
		headers = {
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
			"Cookie":cookie
		}
		return headers