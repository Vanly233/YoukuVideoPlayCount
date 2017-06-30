#! python3
# -*- coding: UTF-8 -*-

# 数据库操作
# 链接数据库：主机host，用户名，密码，数据库名称
# 获取游标对象
# 执行SQL语句
# 获取结果
# 关闭链接

import pymysql

'''
print('username:')
user = input()
print('password:')
password = input()
'''

db_connect = pymysql.connect('localhost', 'root', '839839', 'db_youku')

cursor = db_connect.cursor()

effect_rows = cursor.execute('SELECT * FROM gaobowen')

row_1 = cursor.fetchone()
print(row_1)

row_2 = cursor.fetchmany(6)
print(row_2)

row = cursor.fetchall()
print(row)

print(str(effect_rows))

db_connect.commit()

cursor.close()

db_connect.close()

