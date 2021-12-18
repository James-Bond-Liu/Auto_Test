# -*- coding: utf-8 -*-
# @Time :2020/6/16 19:35
# @Author : liufei
# @File :http_request_unittest_new1.PY

import unittest
from 数据处理.dfghjk import http_request_unittest_new1
import HTMLTestRunnerNew

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(http_request_unittest_new1))
with open('http_request_test_report01.html','wb',encoding='utf-8') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='http_request测试报告', description=None, tester='刘菲')
    runner.run(suite)