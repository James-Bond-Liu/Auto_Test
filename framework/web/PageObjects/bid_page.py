 # -*- coding: utf-8 -*-
# @Time :2020/8/9 16:38
# @Author : liufei
# @File :bid_page.PY

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.web.PageLocators.bidpage_locators import BidPageLocators as loc

class BidPage():

    def __init__(self, driver):
        self.driver = driver

    #投资
    def invest(self, money):
        #输入投资金额，
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.money_input))
        self.driver.find_element(*loc.money_input).send_keys(money)
        #点击投资按钮
        self.driver.find_element(*loc.invest_button).click()

    #获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.money_input))
        return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    #投资成功的提示框-点击查看激活
    def click_activeButton_on_success_popup(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.active_button_on_successPop))
        self.driver.find_element(*loc.active_button_on_successPop).click()

    #错误提示框-页面中间
    def get_erroMsg_from_pageCenter(self):
        #获取文本内容
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.invest_failed_popup))
        msg = self.driver.find_element(*loc.invest_failed_popup).text()
        # 关闭弹出框
        self.driver.find_element(*loc.invest_failed_popup).click()
        return msg

    #获取提示信息-投标按钮
    def get_errorMsg_from_investButton(self):
        pass

#刘菲
