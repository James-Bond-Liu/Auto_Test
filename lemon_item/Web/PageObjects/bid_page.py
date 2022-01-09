 # -*- coding: utf-8 -*-
# @Time :2020/8/9 16:38
# @Author : liufei
# @File :bid_page.PY

from lemon_item.Web.PageLocators.bidpage_locators import BidPageLocators as loc
from lemon_item.Web.Common.basepage import BasePage

class BidPage(BasePage):

    #投资
    def invest(self, money):
        #输入投资金额
        doc = '投资页面-金额投资输入框'
        self.wait_eleVisable(loc.money_input, doc=doc)
        self.input_text(loc.money_input, money, doc)
        #点击投资按钮
        self.click_element(loc.money_input, doc)

    #获取用户余额
    def get_user_money(self):
        doc = '投资页面-用户余额'
        self.wait_eleVisable(loc.money_input)
        self.get_element_attribute(loc.money_input, doc, "data-amount")

    #投资成功的提示框-点击查看激活
    def click_activeButton_on_success_popup(self):
        doc = "....."
        self.wait_eleVisable(loc.active_button_on_successPop)
        self.click_element(loc.active_button_on_successPop, doc)

    #错误提示框-页面中间
    def get_erroMsg_from_pageCenter(self):
        doc = "....."
        # 获取文本内容
        self.wait_eleVisable(loc.invest_failed_popup)
        self.get_eleText(loc.invest_failed_popup, doc)
        # 关闭弹出框
        self.click_element(loc.invest_failed_popup, doc)

    #获取提示信息-投标按钮
    def get_errorMsg_from_investButton(self):
        pass
