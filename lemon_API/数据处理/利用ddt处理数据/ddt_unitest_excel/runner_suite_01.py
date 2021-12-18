# -*- coding: utf-8 -*-
# @Time :2020/6/18 21:22
# @Author : liufei
# @File :test_suite.PY

import unittest
import HTMLTestRunnerNew
from 数据处理.利用ddt处理数据.ddt_unitest_excel.test_case import TestHttp

#当测试用例中采用ddt装饰后，在执行测试用例模块中，只能采用loader加载测试用例进而执行用例。不能采用将测试用例实例化的方法执行测试用例
#loader加载测试用例
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttp))
#执行
with open('test_suite.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title=None,description=None,tester=None)
    runner.run(suite)