#! python3

import requests
import time

count_pv = 0
count_clk = 0

# url_pv = 'http://ad.thepaper.cn/s?z=paper&c=2037&op=1'
# url_pv = 'http://g.cn.miaozhen.com/x/k=6003218&p=6LX&met=0&rt=2&mo=__OS__&ns=__IP__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&v=__LOC__&vv=1&o='
# url_pv = 'http://0cf74833b323.ih5.cn/idea/CzjLeF7?vxparm=/vxid_1/senderid_464259cd0e064cb1&source=ohAJ7wdDZDibOiDJnn4Da5dB6WiA&suid=524E61BF-6033-4164-986D-318F11C7F725&sl=0'
# url_clk = 'http://ad.thepaper.cn/c?z=paper&la=0&si=44&cg=309&c=2037&ci=37&or=271&l=2057&bg=2057&b=4065&u=http://www.thepaper.cn/list_26525'
# url_clk = 'http://ad.thepaper.cn/c?z=paper&la=0&si=44&cg=309&c=1960&ci=37&or=1723&l=3376&bg=3376&b=7311&u=http://e.cn.miaozhen.com/r/k=6003218&p=6LX&met=0&rt=2&mo=__OS__&ns=__IP__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&v=__LOC__&vo=37c74daf9&vr=2&o=https://m.ihg.com/hotels/crowneplaza/cn/zh/findandbook?cm_mmc=MOSMGC-CP-CN-ZH-CPPromo2017-TheP_1'
url_clk = 'http://c.eqxiu.com/s/X4Ru4eWb' #'http://v.youku.com/v_show/id_XODk3NzYyNTUy.html'

#headers_iphone = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4'}
headers_wechat = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.556.400 QQBrowser/9.0.2524.400'}
headers_chrome = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

for i in range(1000):
	#res_pv = requests.get(url_pv, headers = headers_wechat)
	#print('pv requests')
	#if res_pv.status_code == 200:
		#count_pv += 1
		#print('pv ok')
	res_clk = requests.get(url_clk, headers = headers_chrome)
	#print('clk requests')
	if res_clk.status_code == 200:
		count_clk += 1
		print('clk ok')

	i += 1

	print(i)
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())));
	print("------------")
	print("pv: \t" + str(count_pv))
	print("clk:\t" + str(count_clk))
	time.sleep(5)
