# -*- coding: utf-8 -*-
# @Time :2020/6/18 21:22
# @Author : liufei
# @File :test_suite.PY

import unittest
import HTMLTestRunnerNew
from 数据处理.测试用例参数化.test_case import TestHttp

test_data=[{'url':'http://ip:8080/futureloan/mvc/api/member/login','method':'get',
            'data':{'name': '15631128476','passwd':'www.950620.cn'},'expected':'10001'},
           {'url':'http://ip:8080/futureloan/mvc/api/member/login','method':'get',
            'data':{'name': '15631128476','passwd':'www.950620.cn'},'expected':'10001'},
           {'url':'http://ip:8080/futureloan/mvc/api/member/recharge','method':'get',
            'data':{'name': '15631128476','passwd':'www.950620.cn'},'expected':'20117'},
           {'url':'http://ip:8080/futureloan/mvc/api/member/recharge','method':'get',
            'data':{'name': '15631128476','passwd':'www.950620.cn'},'expected':'20117'}]

suite=unittest.TestSuite()
for item in test_data:
    suite.addTest(TestHttp('test_api',item['url'],item['method'],item['data'],item['expected']))

with open('test_suite.html','wb',encoding='utf-8') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title=None,description=None,tester=None)
    runner.run(suite)