# -*- coding: utf-8 -*-
# @Time :2020/7/18 9:17
# @Author : liufei
# @File :runner.PY

import unittest
from lemon_item.API1.common.test_http_request import TestHttpRequest
from lemon_item.API1.common.get_path import *
import HTMLTestRunnerNew

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
with open(test_result_html_path, 'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='前程贷API项目测试报告',description=None,tester='刘菲')
    runner.run(suite)
