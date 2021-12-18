# -*- coding: utf-8 -*-
# @Time :2020/6/18 21:14
# @Author : liufei
# @File :test_suite.PY

import unittest
from 数据处理.读取execl的三种方法.http_request import HttpRequest
from 数据处理.读取execl的三种方法.get_data import GetData

class TestHttp(unittest.TestCase):
    def __init__(self,methodName,url,method,data,expected):
        super(TestHttp,self).__init__(methodName)  #此处利用了超继承的方法
        self.url=url
        self.method=method
        self.data=data
        self.expected=expected
    def test_api(self):
        res=HttpRequest().http_request(self.url, self.method, self.data,getattr(GetData,'cookie'))
        if res.cookies:
            setattr(GetData,'cookie',res.cookies)
        try:
            self.assertEqual(self.expected,res.json()['code'])
        except AssertionError as e:
            print('test_api error is {}'.format(e))


