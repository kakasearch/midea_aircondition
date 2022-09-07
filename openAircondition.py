import requests
import datetime
import time
def powerIsOn():
	#查询空调状态，返回电源是否打开
	api = "https://mp-prod.smartmidea.net:443/mas/v5/app/proxy?alias=/v1/appliance/shadow/{$applianceCode，抓包获取}?reqId={$ reqId，抓包获取}&queryType=both"
	headers = {
		"Host":"mp-prod.smartmidea.net:443",
		"appid":"900",
		"Accept":"*/*",
		"version":"8.10.0",
		"secretVersion":"1",
		"Accept-Language":"zh-CN,zh-Hans;q=0.9",
		"Accept-Encoding":"gzip, deflate, br",
		"platform":"1",
		"accessToken":"{$ your token}",
		"Content-Type":"application/json",
		"User-Agent":"mei de mei ju/8.10.0(iPhone;iOS 15.5; Scale/2.00)",
		"Connection":"keep-alive",
		"Cookie":"{$ your Cookie}"
	}
	r = requests.get(api,headers=headers)
	#print(r.text) #{"code":0,"msg":"success","data":{"applianceCode":123123123,"sn":"0000001231230000","level":3,"expect":"","shadow":{"targetTemperature":21.0,"power":false,"windSpeed":102,"runMode":"cool"},"difference":"","updateTime":123123}}
	return r.json()["data"]["shadow"]["power"]

def openAircondition():
	#打开空调
	api = 'https://xiaodu.baidu.com/saiya/smarthome/directivesend?from=h5_control'
	headers = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX3161 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 FromApp/XiaoDuApp oneapp/4.1.0.1 sdk/0.7.0',
		'Content-Type': 'application/json;charset=UTF-8',
		'Accept': '*/*',
		'Origin': 'https://xiaodu.baidu.com',
		'X-Requested-With': 'com.baidu.duer.superapp',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://xiaodu.baidu.com/saiya/smarthome/index.html',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
		'Cookie': '{$ your Cookie}',
	}
	data = '''{"header":{"namespace":"DuerOS.ConnectedHome.Control","name":"TurnOnRequest","payloadVersion":1},"payload":{"appliance":{"applianceId":["{$设备id，同applianceCode，抓包获取}"]}}}'''
	r = requests.post(api,headers=headers,data=data)
	# print(r.text)
	if r.json()["status"] == 0:
		return True
	else:
		return False


if __name__ == '__main__':
	if powerIsOn():
		print("空调已经打开")
	else:
		print("空调已关闭，正在尝试打开")
		if openAircondition():
			print("空调打开成功")
		else:
			print("空调打开失败")
		
