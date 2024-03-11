# -*- coding: utf-8 -*-
# @Time :2020/8/14 20:48
# @Author : liufei
# @File :Run.PY

import unittest
import HTMLTestRunnerNew
from framework.web.Common import dir_config

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(dir_config.testcase_dir + r'\test_login'))
with open(dir_config.report_dir) as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, tester='刘菲')
    runner.run(suite)