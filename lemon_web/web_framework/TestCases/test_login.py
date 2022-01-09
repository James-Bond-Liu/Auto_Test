# -*- coding: utf-8 -*-
# @Time :2020/8/6 21:00
# @Author : liufei
# @File :test_login.PY

from selenium import webdriver
import unittest
from lemon_web.web_framework.PageObjects.login_page import LoginPage
from lemon_web.web_framework.PageObjects.index_page import IndexPage
from lemon_web.web_framework.TestDatas import common_data as CD
from lemon_web.web_framework.TestDatas import login_data as LD
from ddt import ddt, data

'''测试用例=测试对象（功能）+测试数据'''
@ddt()
class TestLogin(unittest.TestCase):

    '''
    利用setUpClass/tearDownClass方法，在所有测试用例执行前执行一次setUpClass/tearDownClass方法
    设计思想：异常用例优先于正常用例执行，每次异常用例(不能正常登录进入后面的页面)执行完成之后刷新页面,进行下一次的用例操作
    使用此种方法的前提是每条用例之间要不想不影响
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        cls.lg = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass
    #每执行一条用例结束后刷新浏览器
    def tearDown(self):
        self.driver.refresh()

    #正常用例-登录成功
    def test_2_login_success(self):
        # 步骤：输入用户名密码点击登录
        self.lg.login(LD.success_data['user'], LD.success_data['password'])
        # 断言：页面中能否找到**元素
        self.assertTrue(IndexPage(self.driver).isExist_logout_element())

    #异常用例-手机号格式不正确(大于11位，小于11位，不在号码段，为空）利用ddt操作
    @data(*LD.phone_data)
    def test_0_login_user_wrongformat(self, data1):
        # 步骤：输入用户名密码点击登录
        self.lg.login(data1['user'], data1['password'])
        # 断言：页面中提示请输入正确的手机号
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(), data1['check'])

    #异常用例-手机号时未注册的,不输入密码,错误密码
    @data(*LD.password_data)
    def test_1_login_wrongPwd_noReg(self, data2):
        self.lg.login(data2['user'], data2['password'])
        self.assertEqual(self.lg.get_errorMsg_from_pageCenter(), data2['check'])
