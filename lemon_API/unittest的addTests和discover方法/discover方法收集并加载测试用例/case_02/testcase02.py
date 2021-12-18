# -*- coding: utf-8 -*-
# @Time :2020/8/16 12:02
# @Author : liufei
# @File :test_02.PY

import unittest

class Test_01(unittest.TestCase):
    def setUp(self):
        print('**************开始test_01****************')

    def tearDown(self):
        print('**************结束test_01****************')

    def test_01(self):
        print('aaaaaa')

    def test_02(self):
        print('bbbbbb')

    def test_03(self):
        print('cccccc')
