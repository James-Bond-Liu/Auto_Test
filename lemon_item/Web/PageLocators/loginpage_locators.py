# -*- coding: utf-8 -*-
# @Time :2020/8/8 21:29
# @Author : liufei
# @File :loginpage_locators.PY

from selenium.webdriver.common.by import By

'''
元素的定位类型和定位表达式用元组来管理，形成一个新的分层
'''
class LoginPageLocators():
    #用户名输入框
    name_text = (By.XPATH, '//input[@name="phone"]')
    #密码输入框
    pwd_text = (By.XPATH, '//input[@name="password"]')
    #登录按钮
    login_button = (By.XPATH, '//button[text()="登录"]')
    # 获取错误信息(文本)-页面登录区域
    errorMsg_from_loginArea = (By.XPATH, "//div[@class='form-error-info']")
    # 获取错误信息(文本)-页面正中间
    errorMsg_from_pageCenter = (By.XPATH, "//div[@class='layui-layer-content']")