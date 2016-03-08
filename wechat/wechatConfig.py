#! /usr/bin/python
# -*- coding: utf-8 -*-
from flask import make_response
import hashlib
from mode import scanPort,sendSMS,queryData

def wechat_auth(token,data):
	signature = data.get('signature','')
	timestamp = data.get('timestamp','')
	nonce = data.get('nonce','')
	echostr = data.get('echostr','')
	s = [timestamp,nonce,token]
	s.sort()
	s = ''.join(s)
	if (hashlib.sha1(s).hexdigest() == signature):
	    return make_response(echostr)

def wechat_mode(content):
	if content==u"攻击":
		return "G1:端口扫描\nG2:短信攻击\nG3:社工库\n\n攻击格式：编号&目标\n列如：G1&127.0.0.1\n列如：G2&188****1111\n列如：G3&mail(QQ|mail|phone):test@163.com"
	elif  "G1&" in content:
		arr=content.split('&')
		return "你扫描的IP端口为："+str(scanPort.init(arr[1]))
	elif  "G2&" in content:
		arr=content.split('&')
		return "系统提示："+str(sendSMS.sendSMS(arr[1]))
	elif  "G3&" in content:
		arr=content.split('&')
		arrss=''
		if "QQ:" in arr[1]:
			arrs=arr[1].split(':')
			arrss=arrs[1]
		elif "mail" in arr[1]:
			arrs=arr[1].split(':')
			arrss=arrs[1]
		elif "phone" in arr[1]:
			arrs=arr[1].split(':')
			arrss=arrs[1]

		return "你的丢失数据有："+str(queryData.queryData(arrss))
	else:
		return "感谢你的留言！"
