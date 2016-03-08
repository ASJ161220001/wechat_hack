#! /usr/bin/python
# -*- coding: utf-8 -*-
import socket #socket包
import threading #线程包

#全局变量
RESULT=[]
IP=''

#判断端口是否存在
def isPort(port):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET 是 IPv4 网络协议的套接字类型   SOCK_STREAM即TCP协议
        sk.settimeout(1) #超时时间
        try:
            sk.connect((IP,port)) #开始连接
            RESULT.append(port)
        except Exception:
                return '没有此端口！' 
        sk.close() #关闭

#创建线程，需要多少端口就创立多少线程，速度抗抗的
def main(ports):
    threadpool=[] #线程数组

    for p in ports:
        th = threading.Thread(target= isPort,args= [p]) #target 方法名字 args 单个参数 可以用 [p] or (p,)  多个参数（p,a,b)
        threadpool.append(th) #线程数组添加线程

    for th in threadpool:
        th.setDaemon(True) #守护线程
        th.start() #启动线程

    for th in threadpool: 
        threading.Thread.join(th) 

def init(ip):
    IP=ip
    del RESULT[:]
    ports=[80,8080,3128,8081,3306,9080,1080,21,23,443,69,22,25,110,7001,9090,3389,1521,1158,2100,1433] #扫描端口
    main(ports)
    return  RESULT

