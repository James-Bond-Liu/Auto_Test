# -*- coding: utf-8 -*-
# @Time :2020/8/6 20:35
# @Author : liufei
# @File :login_page.PY

from Web.PageLocators.loginpage_locators import LoginPageLocators as loc
from Web.Common.basepage import BasePage

'''登录页面'''
class LoginPage(BasePage):

    #登录
    def login(self, username, password, remember_user=False):
        #输入用户名
        #输入密码
        #点击
        doc = "登录页面—登录区域"
        self.wait_eleVisable(locator=loc.name_text, doc=doc)
        self.input_text(loc.name_text, username, doc)
        self.input_text(loc.pwd_text, password, doc)
        self.click_element(loc.login_button, doc)

    #注册
    def register_enter(self):
        doc = "注册区域"
        self.wait_eleVisable("", doc=doc)
        self.click_element("", doc)

    #获取错误提示信息(文本)-登录区域
    def get_errorMsg_from_loginArea(self):
        doc = "登录区域"
        self.wait_eleVisable(locator=loc.errorMsg_from_loginArea, doc=doc)
        return self.get_eleText(locator=loc.errorMsg_from_loginArea, doc=doc)

    #获取错误信息(文本)-页面正中间
    def get_errorMsg_from_pageCenter(self):
        doc = "登录页面-页面正中间"
        self.wait_eleVisable(locator=loc.errorMsg_from_pageCenter, doc=doc)
        return self.get_eleText(locator=loc.errorMsg_from_pageCenter, doc=doc)
