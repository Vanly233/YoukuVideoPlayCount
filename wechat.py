#！Python3
#*--coidng=utf8--*

import itchat
#from itchat.content import *

itchat.auto_login()
user = itchat.search_friends(name=u'官宾宾')[0]
user.send(u'这是一条测试信息，请忽略')
