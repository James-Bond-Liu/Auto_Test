# -*- coding: utf-8 -*-
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from  datetime import datetime, timedelta
import time

class GlobalData():
    """ESS_API测试数据"""
    ess_url = 'http://192.168.108.160:'
    api_url = 'http://192.168.108.160:8081'
    token = None
    cookies = None
    downPrice_id = None
    upPrice_id = None
    powerStation_id = None
    customer_id = None
    customer_no = None
    operator_no = None
    organization_id = None
    organization_code = None

    """ 第三方API测试数据"""
    ThirdUserToken = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjdXN0b21lci0wMDAwMDAwMDAwMDAwMDAiLCJjb2RlIjoibmJwIiwidG9rZW5JZCI6MjYyMzI0MzI1NzIwMDY0LCJleHAiOjQwOTUzMDk5NzIsImlhdCI6MTY5NjkzMjM4Niwib3duZXJfdHlwZSI6InRlbXBvcmFyeSIsImxvY2FsIjoiZW4ifQ.nf7enaHsUz7v9Ik29Ck1u_D3OOM4m8OLKuAVITBq45agiqerivjBMgKtMoGV1Gz__Kcp4MZ_U30taJWEhuiD3g"
    secuid = None
    key = None
    # 逆变器
    thirdSite_id = 21
    thirdDevice_id = 26
    thirdSn_number = 'ThirdApi_sn2'
    # 充电桩
    thirdSite_id_charge = None
    thirdDevice_id_charge = None
    thirdSn_number_charge = None
    downPrice_id_charge = None
    upPrice_id_charge = None
    #当前时间两天前的零时时间戳毫秒级
    m1 = (datetime.now() + timedelta(days=-2)).strftime('%Y-%m-%d')
    startTimel= round(time.mktime(time.strptime(m1, "%Y-%m-%d")) * 1000)
    # 当前时间的零时时间戳毫秒级
    n1 = (datetime.now() + timedelta(days=0)).strftime('%Y-%m-%d')
    endTimel = round(time.mktime(time.strptime(n1, "%Y-%m-%d")) * 1000)
    # 格式yy-mm-dd
    m2 = (datetime.now() + timedelta(days=-5)).strftime('%Y-%m-%d')
    n2 = (datetime.now() + timedelta(days=0)).strftime('%Y-%m-%d')
    startTimes1 = m2
    endTimes1 = n2
    # 格式yymmdd
    w2 = (datetime.now() + timedelta(days=-5)).strftime('%Y%m%d')
    t2 = (datetime.now() + timedelta(days=0)).strftime('%Y%m%d')
    startTimes2 = w2
    endTimes2 = t2

if __name__ == '__main__':
    print(GlobalData().startTimes)
    print(GlobalData().endTimes)


