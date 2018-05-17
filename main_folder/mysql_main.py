#! /usr/bin/env python
# -*- coding=utf-8 -*-

import pymysql

# 连接数据库
def load_mysqldb():
    print("连接到服务器...")
    com = pymysql.connect("localhost", "root", "modi123456", "FORMUALDB")
    print("连接成功")
    return com


