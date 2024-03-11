# -*- coding: utf-8 -*-
# @Time :2020/6/16 19:46
# @Author : liufei
# @File :http_request_unittest_new1.PY

'''
用映射,设置充值请求中的cookie
'''
import unittest
from 基础语法.api.unittest.测试用例数据交互.http_request import HttpRequest
from 基础语法.api.unittest.测试用例数据交互.get_data import GetData

class http_request_login(unittest.TestCase):
    def setUp(self):
        '''setup函数在每个用例执行之前都会执行一次setup函数。
        将url放在此处，便于后续函数调用，减少代码重复
        '''
        self.login_url = 'http://ip:8080/futureloan/mvc/api/member/login'
        #只有加上self，在类后面的方法函数中才可以调用这个属性
        self.recharge_url='http://ip:8080/futureloan/mvc/api/member/recharge'

    def test_login_normal(self):
        data = {'name': '15631128476', 'passwd': 'www.950620.cn'}
        res=HttpRequest().http_request(self.login_url,'get',data)
        if res.cookies:#如果cookie有的话就更新cookie
            setattr(GetData,'cookie',res.cookies)#利用全局变量的方法更新cookie
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
        print('没有密码的情况',res)

    #充值请求的cookie来自于get_data.py中的cookie，利用了反射。
    def test_recharge_normal(self):
        recharge_data = {'name':'15631128476','amount': '1000'}
        recharge_res=HttpRequest().http_request(self.recharge_url,'post',recharge_data,getattr(GetData,'cookie'))  #利用反射
        try:
            self.assertEqual('10001', recharge_res.json()['code'])
        except AssertionError as e:
            print(' test_recharge_normal error is {}'.format(e))
            raise e

    def test_recharge_negative(self):
        recharge_data = {'name':'15631128476','amount': '-1000'}
        recharge_res = HttpRequest().http_request(self.recharge_url, 'post', recharge_data, getattr(GetData,'cookie'))  #利用反射
        try:
            self.assertEqual('20117',recharge_res.json()['code'])
        except AssertionError as e:
            print(' test_recharge_negative error is {}'.format(e))
            raise e

    def tearDown(self):
        pass
