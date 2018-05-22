#! /usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
import xlwt
import xlrd
import pandas
import numpy


'''
连接数据库块'workspace_db,通过游标fech数据

'''

# 连接数据库
print("连接到服务器...")
com = pymysql.connect(host='localhost', port=3306, user='root', passwd='modi123456', 
db='work db', charset='utf8')

# 获取游标
cursor_db = com.cursor()

cursor_db.execute()

'''
导入/导出表格
'''
def load_excel():
    