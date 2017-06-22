#! python3
# -*- coding: UTF-8 -*-

import pymysql

db = pymysql.connect('localhost','root','839839','db_ad');

cursor = db.cursor()

cursor.execute('SELECT * FROM tb_user')

data = cursor.fetchall()

print('%s' % data)

db.close()