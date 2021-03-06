# -- coding:utf-8--
import socket
import time
import datetime
import json
import os

def timeyz(tiz):
	yzjg = False
	timex = now_time()
	if tiz > timex:
		yzjg = True
	else:
		yzjg = False
	return yzjg


def now_time():
	#用于获取当前时间的函数
	nowtime=datetime.datetime.now()
	timexx = nowtime.strftime('%Y-%m-%d-%H-%M')
	return timexx

def now_time_show():
	#用于获取当前时间的函数
	nowtime=datetime.datetime.now()
	timexx_show = nowtime.strftime('%Y-%m-%d-%H-%M-%S')
	return timexx_show


def wl_time(z):
	#生成未来时间的函数
	nowtime=datetime.datetime.now()
	detaday=datetime.timedelta(days=z)
	da_days=nowtime+detaday
	wltime = da_days.strftime('%Y-%m-%d-%H-%M')
	#输出返回值为 年 月 日 时 分
	return wltime



def yzkey_keyk(key):
	#验证密钥库
	keyklj = "key.json"
	fhz = ""

	#打开密钥库
	with open(keyklj) as zx:
		keyk = json.load(zx)

	#判断密钥是否在密钥库中
	if key in keyk.keys():
		#获取密钥时间
		keytime = keyk[key]
		#将密钥时间转换为统一格式
		wl_time_sr = wl_time(keytime)
		#删除密钥库中的已用密钥
		del keyk[key]
		#写入到json文件中
		with open(keyklj,'w') as ojbk_1:
			json.dump(keyk,ojbk_1)
		fhz = "True"
		usertime = wl_time_sr
	else:
		fhz = "False"
		usertime = "0000-00-00-00-00"

	return fhz, usertime



def yzkey_userk(uuid):
	#验证用户信息库
	userklj = "userk.json"
	fhz = "0"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)
	#验证key是否存在
	if uuid in userk.keys():
		user_xx = userk[mac]
		#取得用户预存密钥
		time = user_xx[0]
		root = user_xx[1]
		x = user_xx[4]
		#查看时间是否有效
		if timeyz(time):
			ztm = "1"
		else:
			ztm = "3"
	else:
		ztm = "2"
		time = "0000-00-00-00-00"
		root = False
		x = "0"
	return ztm, time, root, x

