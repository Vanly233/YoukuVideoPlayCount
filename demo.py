#! python3

import requests
import json
import re
import time
import openpyxl

'''
id = ['XMjc4NDM4MDU3Mg',		#高博文
		'XMjc3MTkyNTEyNA',		#包一峰
		'XMjc2NTc3OTQ2NA',		#姜鹏
		'XMjc0MDQxNDIzMg',		#叶泳湘
		'XMjcxNDU5NTM1Ng'		#马薇薇	
];
'''

def getVV():
	id = ['696095143',
			'692981281',
			'691444866',
			'685103558',
			'678648839'
		];	#视频ID

	url1 = 'http://v.youku.com/action/getVideoPlayInfo?beta&timestamp=&vid=';		#js请求前部
	url2 = '&showid=0&param[]=share&param[]=favo&param[]=download&param[]=phonewatch&param[]=updown&callback=tuijsonp4';	#js请求后部
	for i in range(len(id)):
		url = url1 + id[i] + url2;
		#print(id[i]);
		res = requests.get(url);
		jsonRegex = re.compile(r'{.*}');	#从请求响应中正则出json报文
		mo = jsonRegex.search(res.text);
		#print(mo.group());
		jsonData = json.loads(mo.group());	#str转为dict
		data = jsonData.get('data', -1);
		stat = data.get('stat', -1);
		vv = stat.get('vv', -1);
		print(vv);
		#print(type(vv));

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

pause = sleeptime(0,5,0);
while 1==1:
	print(time.strftime('%Y-%m-%d %H:%I:%M',time.localtime(time.time())));
	getVV();
	time.sleep(pause);



