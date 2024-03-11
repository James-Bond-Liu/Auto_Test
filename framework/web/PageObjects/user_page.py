# -*- coding: utf-8 -*-
# @Time :2020/8/9 16:37
# @Author : liufei
# @File :user_page.PY

from framework.web.Common.basepage import BasePage
from framework.web.PageLocators.userpage_locators import UserPageLocators as loc

class UserPage(BasePage):

    #获取用户余额
    def get_user_leftMoney(self):
        doc = '个人页面-获取用户余额'
        #等待元素
        self.wait_eleVisable(locator=loc.user_leftMoney, doc=doc)
        #获取个人可用余额的文本内容
        text = self.get_eleText(locator=loc.user_leftMoney, doc=doc)
        #截取数字部分，分隔符“元”
        return text.strip('元')

    #获取第一条投资记录的时间、金额、收益金额，
    def get_first_investRecord_info(self):
        pass