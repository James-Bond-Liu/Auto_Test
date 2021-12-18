# -*- coding: utf-8 -*-
# @Time :2020/8/10 19:35
# @Author : liufei
# @File :bidpage_locator.PY

from selenium.webdriver.common.by import By

class BidPageLocators():
    #投资金额输入框
    money_input = (By.XPATH, '//input[@name="phone"]')
    #投资成功提示框
    active_button_on_successPop = (By.XPATH, '//input[@name="phone"]')
    #投资失败提示框
    invest_failed_popup = (By.XPATH, '//input[@name="phone"]')