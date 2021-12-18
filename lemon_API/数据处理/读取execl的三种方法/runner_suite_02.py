# -*- coding: utf-8 -*-
# @Time :2020/6/20 15:09
# @Author : liufei
# @File :runner_suite_02.PY
#根据坐标取值的时候必须保证，excel中的数据和参数实际是对应的
import unittest
import HTMLTestRunnerNew
from 数据处理.读取execl的三种方法.test_case import TestHttp
from 数据处理.读取execl的三种方法.do_excel_02 import GetTestData

t=GetTestData('data_01-02.xlsx', 'request_data')

suite=unittest.TestSuite()
for i in range(1,t.max_row+1):
    suite.addTest(TestHttp('test_api',t.get_data(i,1),t.get_data(i,2),eval(t.get_data(i,3)),str(t.get_data(i,4))))

with open('test_suite.html','wb',encoding='utf-8') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title=None,description=None,tester=None)
    runner.run(suite)