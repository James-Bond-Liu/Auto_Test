# -*- coding: utf-8 -*-
# @Time :2020/8/16 11:43
# @Author : liufei
# @File :加载测试用例的另一种方法.PY

import unittest

class Test1(unittest.TestCase):
    def test_01(self):
        print('111111')

    def test_02(self):
        print('222222')

    def test_03(self):
        print('333333')

class Test2(unittest.TestCase):
    def test_01(self):
        print('aaaaaa')

    def test_02(self):
        print('bbbbbb')

    def test_03(self):
        print('cccccc')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    #将用例添加在一起形成一个列表集合
    case_list = [Test1('test_01'), Test1('test_02'), Test1('test_03'),
                 Test2('test_01'), Test2('test_02'), Test2('test_03')]
    #addTests方法加载测试用例集合
    suite.addTests(case_list)
    runner = unittest.TextTestRunner()
    runner.run(suite)