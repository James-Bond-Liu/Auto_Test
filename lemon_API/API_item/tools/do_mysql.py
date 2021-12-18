# -*- coding: utf-8 -*-
# @Time :2020/7/5 15:45
# @Author : liufei
# @File :do_mysql.PY

import pymysql
from API_item.tools.project_path import *
from API_item.tools.read_config import ReadConfig

class DoMysql():
    def do_mysql(self,query_sql,state='all'):#query_sql表示查询语句，all——多条，1——一条
        #连接数据库所需要的信息
        # db_config={'host':'47.107.168.87','user':'scott','password':'123456','database':'future'}

        #创建数据库连接
        db_config=eval(ReadConfig.get_config(test_config_path,'DB','db_config'))
        cnn=pymysql.connect(**db_config)   #关键字参数可以通过“**变量”字典的形式传入

        #创建游标
        cursor=cnn.cursor()

        # #写sql语句——字符串格式
        # query_sql='select max(mobilephone) from member where MobilePhone'

        #执行sql语句
        cursor.execute(query_sql)

        #获取结果
        if state==1:
            res=cursor.fetchone()   #返回元组格式，针对一行数据使用。当有多条数据返回时默认取第一条（即游标所在的行），或者用for循环将所有数据全部取出
        else:
            res=cursor.fetchall()  #返回列表嵌套元组的数据格式，针对多行数据使用。
        #关闭游标
        cursor.close()
        #关闭数据库连接
        cnn.close()

        return res
if __name__ == '__main__':
    res=DoMysql().do_mysql('select * from user',1)
    print(res[0])
