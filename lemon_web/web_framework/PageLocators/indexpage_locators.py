# -*- coding: utf-8 -*-
# @Time :2020/8/10 19:29
# @Author : liufei
# @File :Indexpage_locators.PY

from selenium.webdriver.common.by import By

class IndexPageLocators():
    #用户昵称
    user_link = (By.XPATH, '//a[@href="/Member/index.html"]')

    #抢投标按钮
    bid_button = (By.XPATH, '//a[@class="btn btn-special"]')