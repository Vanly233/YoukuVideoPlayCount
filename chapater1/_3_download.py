
import urllib2

def download(url, num_retries=2):
	print '下载:' ,url;
	try:
		html = urllib2.urlopen(url).read();
	except urllib2.URLError as e:
		print '下载错误:', e.reason ;
		html = None;
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <= e.code <600:
				#print(str(e.code));
				return download(url, num_retries-1);
	return html;
	

print(download('http://v.youku.com/v_show/id_XMjcxNDU5NTM1Ng==.html'));
