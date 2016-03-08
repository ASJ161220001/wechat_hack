#! /usr/bin/python
# -*- coding: utf-8 -*-
import time
from flask import Flask,g,request,make_response
import hashlib
import xml.etree.ElementTree as ET
from wechat import wechatConfig

app = Flask(__name__)

@app.route('/tools',methods=['GET','POST'])
def tools():
	if request.method == 'GET':
		token='wechat'
		return wechatConfig.wechat_auth(token,request.args)
	else:
		req = request.stream.read()
		resultData = ET.fromstring(req)

		toUser = resultData.find('ToUserName').text
		fromUser = resultData.find('FromUserName').text
		content = resultData.find('Content').text

		resultContent = wechatConfig.wechat_mode(content)

		formData = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
		response = make_response(formData % (fromUser,toUser,str(int(time.time())),'text', resultContent))
		response.content_type='application/xml'
		return response

#if __name__ == '__main__':
#    app.run(host="127.0.0.1",port=8001, debug=True)
