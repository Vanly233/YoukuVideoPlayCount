#! python3

import requests,bs4

id = ['XMjc4NDM4MDU3Mg',		#高博文
		'XMjc3MTkyNTEyNA',		#包一峰
		'XMjc2NTc3OTQ2NA',		#姜鹏
		'XMjc0MDQxNDIzMg',		#叶泳湘
		'XMjcxNDU5NTM1Ng'		#马薇薇	
];

url1 = 'http://v.youku.com/v_show/id_';
url2 = '==.html';
for i in range(len(id)):
	url = url1 + id[i] + url2;
	print(url);
#res = requests.get('');

