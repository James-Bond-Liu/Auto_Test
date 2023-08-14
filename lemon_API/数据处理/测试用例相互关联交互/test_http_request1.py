# -*- coding: utf-8 -*-
# @Time :2020/6/16 19:05
# @Author : liufei
# @File :http_request_unittest_new.PY

#将cookie放在setup函数中,在充值用例执行之前会先执行setup函数，这样充值用例可以调用setup中的cookie
import unittest
from 数据处理.测试用例相互关联交互.http_request import HttpRequest

class http_request_login(unittest.TestCase):
    def setUp(self):
        '''setup函数，在每个用例执行之前都会执行一次setup函数。
        将url放在此处，便于后续函数调用，减少代码重复
        '''
        self.login_data = {'name': '15631128476', 'passwd': 'www.950620.cn'}  # 实例变量，这样可以在类中的其他方法调用。相当于扩大了变量的作用范围
        self.login_url = 'http://ip:8080/futureloan/mvc/api/member/login'
        self.login_cookies=HttpRequest().http_request(self.login_url,'get',self.login_data).cookies
        self.recharge_url='http://ip:8080/futureloan/mvc/api/member/recharge'

    def test_login_normal(self):
        data = {'name': '15631128476', 'passwd': 'www.950620.cn'}
        res=HttpRequest().http_request(self.login_url,'get',data)
        try:
            self.assertEqual('10001',res.json()['code'])
        except AssertionError as e:
            print(' test_login_normal error is {}'.format(e))
            raise e
        #登录成功返回  {'data':None,'code':'10001','status':1,'msg':'登录成功'}

    def test_login_wrong_pwd(self):
        data = {'name': '15631128476','pwd':'45223546'}
        res = HttpRequest().http_request(self.login_url, 'get', data)
        try:
            self.assertEqual('20001',res.json()['code'])
        except AssertionError as e:
            print(' test_login_wrong_pwd error is {}'.format(e))
            raise e  #在异常处理时，如果抓到了异常，必须抛出，否则影响用例的准确度

    #充值请求的cookie来自于setup函数
    def test_recharge_normal(self):
        recharge_data = {'name':'15631128476','amount': '1000'}
        recharge_res=HttpRequest().http_request(self.recharge_url,'post',recharge_data,self.login_cookies)
        try:
            self.assertEqual('10001', recharge_res.json()['code'])
        except AssertionError as e:
            print(' test_recharge_normal error is {}'.format(e))
            raise e

    def test_recharge_negative(self):
        recharge_data = {'name':'15631128476','amount': '-1000'}
        recharge_res=HttpRequest().http_request(self.recharge_url, 'post', recharge_data, self.login_cookies)
        try:
            self.assertEqual('20117',recharge_res.json()['code'])
        except AssertionError as e:
            print(' test_recharge_negative error is {}'.format(e))
            raise e

    def tearDown(self):
        pass
