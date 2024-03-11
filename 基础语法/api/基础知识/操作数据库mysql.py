# -*- coding: utf-8 -*-
# @Time :2020/7/4 20:08
# @Author : liufei
# @File :nine.PY

import pymysql

#建立数据库连接
db = pymysql.connect(host="数据库地址",
                     user="用户名",
                     password="密码",
                     port=3306,# 端口
                     database="数据库名",
                     charset='utf8')

#创建游标
cursor = db.cursor()

#执行query_sql的sql语句
query_sql='select * from emp;'
cursor.execute(query_sql)

res=cursor.fetchall() # Python查询Mysql使用fetchall() 方法获取多条数据。
res=cursor.fetchone() # Python查询Mysql使用 fetchone() 方法获取单条数据
print(res)

#关闭游标
cursor.close()

#关闭数据库连接
db.close()
