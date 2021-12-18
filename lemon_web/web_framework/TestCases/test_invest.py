# -*- coding: utf-8 -*-
# @Time :2020/8/9 16:59
# @Author : liufei
# @File :test_invest.PY

import unittest
from selenium import webdriver
from web_framework.PageObjects.login_page import LoginPage
from web_framework.PageObjects.index_page import IndexPage
from web_framework.PageObjects.user_page import UserPage
from web_framework.PageObjects.bid_page import BidPage
import web_framework.TestDatas.common_data as CD
import web_framework.TestDatas.invest_data as ID
import web_framework.TestDatas.login_data as LD
from web_framework.Common.logging import Logging
import ddt

logging = Logging.do_logging()


@ddt.ddt()
class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("==========用例前置：初始浏览器会话，登录前程贷系统=========")
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        LoginPage(cls.driver).login(LD.success_data['user'], LD.success_data['password'])
        IndexPage(cls.driver).click_first_bid()  # 在投标页面选择第一个标来投资
        cls.bid_page = BidPage(cls.driver)

    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        logging.info("==========用例后置：关闭浏览器会话，清理环境=========")
        cls.driver.quit()

    def test_1_invest_success(self):
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
        logging.info("=======投资用例：正常场景-投资成功======")
        # 标页面，获取投资前的个人余额
        userMoney_beforeInvest = self.bid_page.get_user_money()
        # 标页面，输入投资金额，点击投标按钮
        self.bid_page.invest(ID.success['money'])
        # 标页面，投资成功弹出框，点击查看并激活按钮
        self.bid_page.click_activeButton_on_success_popup()
        # 验证,断言
        # 个人页面，获取用户当前余额
        userMoney_afterInvest = UserPage(self.driver).get_user_leftMoney()
        # 求两个金额进行比较
        invest_money = userMoney_beforeInvest - userMoney_afterInvest
        self.assertEqual(float(invest_money), float(ID.success['money']))

    @ddt.data(*ID.no10)
    def test_invest_failed_no100(self, data):
        pass

    @ddt.data(*ID.wrong_format_money)
    def test_invest_0_failed_no10(self, data):
        logging.info("=======投资用例：异常场景-投资金额非100的整数倍，格式不正确等======")
        # 标页面，获取投资前的个人余额
        userMoney_beforeInvest = self.bid_page.get_user_money()
        # 标页面，输入投资金额，点击投标按钮
        self.bid_page.invest(data['money'])
        # 标页面，获取提示信息
        errorMsg = self.bid_page.get_erroMsg_from_pageCenter()
        # 刷新页面
        self.driver.refresh()
        # 获取用户余额
        userMoney_afterInvest = UserPage(self.driver).get_user_leftMoney()
        # 断言
        self.assertEqual(errorMsg, data['check'])
        self.assertEqual(float(userMoney_afterInvest), float(userMoney_beforeInvest))
