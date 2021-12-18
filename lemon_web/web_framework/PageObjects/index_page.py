# -*- coding: utf-8 -*-
# @Time :2020/8/6 20:35
# @Author : liufei
# @File :index_page.PY

'''登陆成功后的首页'''

from web_framework.PageLocators.indexpage_locators import IndexPageLocators as loc
from web_framework.Common.basepage import BasePage
import random

class IndexPage(BasePage):

    def isExist_logout_element(self):
        '''判断登录后的首页是否存在用户昵称'''
        doc = "首页-退出按钮"
        return self.is_eleExist(loc.user_link, doc=doc)

    #选标操作-默认第一个，注意在元素定位的时候过滤掉不可以投的标
    def click_first_bid(self):
        doc = "首页-点击第一个抢投标按钮"
        self.wait_eleVisable(locator=loc.bid_button, doc=doc)
        self.click_element(loc.bid_button, doc=doc)

    #随机选择一个标
    def click_bid_by_random(self):
        doc = "首页-随机点击抢投标按钮"
        self.wait_eleVisable(locator=loc.bid_button, doc=doc)
        eles = self.get_elements(locator=loc.bid_button, doc=doc)   #找到所有符合定位表达式的标，并存储在一个列表里
        index = random.randint(0,len(eles)-1)  #随机数
        eles[index].click()

