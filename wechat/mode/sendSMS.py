#! /usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
mobile=[]
def sendServer1(phone):
	data = {}
	data['mobile'] = phone
	#定义post的地址
	url = 'http://www.xxxx.com/'
	post_data = urllib.urlencode(data)
	#提交，发送数据
	try:
		req = urllib2.urlopen(url, post_data)
	except:
		print '异常'
	#获取提交后返回的信息
	#print req.read()

def sendSMS(phone):
	if phone in mobile:
		return '每个手机号只可以发送一次'
	else:
		#sendServer1(phone)
		#mobile.append(phone);
		#return '暂不支持短信攻击！'
		return '因国家法律问题，暂关闭短信攻击模块！'
