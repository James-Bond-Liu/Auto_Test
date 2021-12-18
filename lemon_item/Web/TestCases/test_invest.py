# -*- coding: utf-8 -*-
# @Time :2020/8/9 16:59
# @Author : liufei
# @File :test_invest.PY

import unittest

class TestInvest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_invest_success(self):
        '''步骤：
        1
        在首页选标 - -不根据标名，根据抢投标按钮选标，默认第一个标
        2
        标页面 - -获取投资前的用户余额，
        3
        标页面 - -输入投资金额，点击投资按钮，
        4
        标页面 - -点击投资成功的弹出框，查看并激活，进入个人页面，

        断言：
        钱 - -投资后的金额是不是少了投资金额
        个人页面 - -获取投资后的金额，
        投资前的金额 - 投资后的金额 = 投资金额，
        投资记录是否正确？
        利息是否正确？'''
        pass

    def test_invest_failed_no100(self):
        pass

    def test_invest_failed_no10(self):
        pass
