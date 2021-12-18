# -*- coding: utf-8 -*-
# @Time :2021/8/18 20:56
# @Author : liufei
# @File :run.PY

import unittest
from 执行用例的三种方法 import test_case
import HTMLTestRunnerNew

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_case))
with open(r'D:\Python_files\lemon_API\执行用例的三种方法\report.html', 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file)
    runner.run(suite)