# -*- coding: utf-8 -*-
# @Time :2020/7/17 20:46
# @Author : liufei
# @File :do_mysql.PY

import pymysql
from common.do_config import DoConfig
from common.get_path import *

class DoMysql():
    def do_mysql(self,query_sql,mode='all'):
        global res
        db_data = eval(DoConfig().do_config(case_config_path,'DB_DATA','db_data'))
        cn = pymysql.connect(**db_data)
        cursor = cn.cursor()
        cursor.execute(query_sql)
        if mode == 1:
            res = cursor.fetchone()
        elif mode == 'all':
            res = cursor.fetchall()
        else:
            print('输入的获取数据格式不正确')
        cn.close()
        cursor.close()
        return res

