# -*- coding: utf-8 -*-
# @Time :2020/6/21 14:33
# @Author : liufei
# @File :runner_suite_03.PY

import unittest
import HTMLTestRunnerNew
from 数据处理.读取execl的三种方法.test_case import TestHttp
from 数据处理.读取execl的三种方法.do_excel_01 import GetTestData

test_data=GetTestData('data_01-02.xlsx', 'request_data').get_test_data()
suite=unittest.TestSuite()
for item in test_data:
    suite.addTest(TestHttp('test_api',item['url'],item['methond'],eval(item['data']),str(item['expected'])))

with open('test_suite.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title=None,description=None,tester=None)
    runner.run(suite)