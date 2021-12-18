# -*- coding: utf-8 -*-
# @Time :2020/6/18 21:14
# @Author : liufei
# @File :test_suite.PY

import unittest
from 数据处理.利用ddt处理数据.项目实践.http_request import HttpRequest
from 数据处理.利用ddt处理数据.项目实践.get_data import GetData
from ddt import ddt,data
from 数据处理.利用ddt处理数据.项目实践.do_excel_01 import GetTestData

@ddt #利用ddt装饰测试类之后就不需要超继承才能使测试函数传参，使用ddt装饰直接可以传参
class TestHttp(unittest.TestCase):

    test_data=GetTestData('data_01-02.xlsx', 'request_data').get_test_data('all')
    @data(*test_data)
    def test_api(self,item):  #item参数，用来接受将test_data脱掉一层外套后的每一条数据
        res=HttpRequest().http_request(item['url'], item['methond'], eval(item['data']),getattr(GetData,'cookie'))
            #exel中的data已经变成了str格式，此处利用eval()函数将其转换成原本的数据格式
        if res.cookies:
            setattr(GetData,'cookie',res.cookies)
        try:
            self.assertEqual(str(item['methond']),res.json()['code'])
            #将excel中的methond强制转换成str格式，
            #因为request请求，返回实体中(res.json())，code是str格式，断言必须要保证格式相同
        except AssertionError as e:
            print('test_api error is {}'.format(e))


