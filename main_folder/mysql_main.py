#! /usr/bin/env python
# -*- coding=utf-8 -*-

import pymysql

# 连接数据库
def load_mysqldb():
    print("连接到服务器...")
    com = pymysql.connect(host='localhost', port=3306, user='root', password='modi123456', db='WORKDB')
    print("连接成功")
    return com

