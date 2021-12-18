# -*- coding: utf-8 -*-
# @Time :2020/8/16 12:01
# @Author : liufei
# @File :test_01.PY

import unittest

class Test_01(unittest.TestCase):
    def setUp(self):
        print('**************开始test_01****************')

    def tearDown(self):
        print('**************结束test_01****************')

    def test_01(self):
        print('111111')

    def test_02(self):
        print('222222')

    def test_03(self):
        print('333333')