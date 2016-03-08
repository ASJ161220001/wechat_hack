#! /usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import lxml.html
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

def init(email):
	data = {}
	data['search'] = email
	data['vip'] = 1
	data['Bkeys'] = 'd26ac15646a0513e36f19c5a053660e2'
	data['Atokens'] = '250b0cd46ca9d483726035e1fc7536e9'
	#定义post的地址
	url = 'http://www.sheyuns.com/ajax/ajax.php'
	post_data = urllib.urlencode(data)
	#提交，发送数据
	try:
		request = urllib2.Request(url)
		request.add_header('Accept', '*/*')
		request.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
		request.add_header('Connection', 'keep-alive')
		request.add_header('Content-Length', '112')
		request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
		request.add_header('Cookie', '__cfduid=d650c8d4c1e38ab68006b5c0cf11056881456913233; yunsuo_session_verify=5ddc8d1822ee97207d314be51482706f; PHPSESSID=nnb3lct30v12p555eltlgq0an7; CNZZDATA1256243452=1877644279-1456910436-%7C1456910436')
		request.add_header('Host', 'www.sheyuns.com')
		request.add_header('Origin', 'http://www.sheyuns.com')
		request.add_header('Referer', 'http://www.sheyuns.com/')
		request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
		request.add_header('X-Requested-With', 'XMLHttpRequest')
		req = urllib2.urlopen(request, post_data)
		html=req.read()
		url = lxml.html.fromstring(html)
		result = url.xpath('//td')
		resultList=[]
		for r in result:
		        isType=r.text
		        if isType=='None':
		        	print 1
		        elif isType=='[SheYun-WSD]':
		        	print 1
		        elif isType=='[AD]':
		        	print 1
		        elif isType is None:
		        	print 1
		        else:
		        	print resultList.append(isType)
		return resultList
	except:
		print '异常'
	#获取提交后返回的信息
	#print req.read()

def queryData(data):
	result=init(data)
	info=''
	for r in result:
		info+=r+'\n'
	return info


