#!/usr/bin/env python
#coding: UTF-8

import uuid

class idUtil():

	def getUUID(self):
		id=str(uuid.uuid1())
		id=id.replace("-","")
		return id