# -*- coding: utf-8 -*-
# @Time :2020/6/25 17:11
# @Author : liufei
# @File :run.PY

import unittest
from API_item.tools.test_http_request import TestHttpRequest
import HTMLTestRunnerNew
from API_item.tools.project_path import *

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='单元测试报告',description=None,tester='刘菲')
    runner.run(suite)


