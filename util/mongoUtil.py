#!/usr/bin/env python
#coding: UTF-8

from pymongo import MongoClient

class mongoUtil():
	client = MongoClient("mongodb://admin:admin@10.0.0.24:30000/admin")
	def __init__(self,db):
		print("初始化。。。")
		self.db = self.client[db]
		pass

	def insert(self,data,collection):
		print(collection)
		self.db[collection].insert(data)
		print("数据插入成功！")
		pass