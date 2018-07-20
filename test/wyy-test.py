#!/usr/bin/env python
# coding=utf-8

import psycopg2
from config import const


# 初始化数据库参数
db_name = const.DB_NAME
db_host = const.DB_HOST
db_port = const.DB_PORT
db_user = const.DB_USER
db_pass = const.DB_PASS
print(db_name,db_host,db_pass,db_user,db_port)

try:
    # 连接数据库
    conn = psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)

except Exception as e:
    print(e.with_traceback())
    print("数据库连接失败"+ str(e.args))



