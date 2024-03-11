# -*- coding: utf-8 -*-
# @Time :2020/6/16 19:35
# @Author : liufei
# @File :http_request_unittest_new1.PY

import unittest
from 基础语法.api.unittest.测试用例数据交互 import test_case1
import HTMLTestRunnerNew

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_case1))
with open('http_request_test_report1.html','wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='http_request测试报告', description=None)
    runner.run(suite)