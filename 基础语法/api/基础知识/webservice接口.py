# -*- coding: utf-8 -*-
# @Time :2020/10/10 21:16
# @Author : liufei
# @File :的风格和对方.PY

from suds.client import Client
from suds.wsse import *

class WebserviceTest():
    def web_service_test(self, url, data, method):
        if method == 'sendMcode':
            res = Client(url).service.sendMcode(data)
        elif method == 'userResigter':
            res = Client(url).service.userResigter(data)
        elif method == 'verifiedUserAuth':
            res = Client(url).service.verifiedUserAuth(data)
        elif method == 'bindBankCard':
            res = Client(url).service.bindBankCard(data)
        return res #返回调用接口的结果

#创建实例
client = WebserviceTest()

#发送短信
sms_url = 'http://ip:port/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
sms_data = {'client_ip':'127.0.0.0', 'tmpl_id':'1', 'mobile':'15612345678'}
sms_res = client.web_service_test(sms_url, sms_data, 'sendMcode')
print('短信的发送结果为{}'.format(sms_res))