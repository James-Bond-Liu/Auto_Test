# -*- coding: utf-8 -*-
# @Time :2020/8/15 18:30
# @Author : liufei
# @File :conftest.PY
from selenium import webdriver
from Web.PageObjects.login_page import LoginPage
from Web.TestDatas import common_data as CD
import pytest

driver = None
@pytest.fixture(scope='class')   #声明此函数是一个fixture,参数scope代表此fixture的作用域。作用域为类。整个测试类只执行一次。
def access_web():
    #前置操作
    global driver
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)  #yield 分隔线，代表前置条件与后置操作的分隔，并且还用来返回（相当于return）变量参数
                        # 返回参数有的格式为元组或列表形式
    #后置操作
    driver.quit()

@pytest.fixture(scope='function')   #作用域为每一个函数，每个函数均会执行一次本函数。
def refresh_page():
    global driver
    yield  #yield不是不许存在的，当存在后置操作时则需要输入yield分割线
    #后置操作
    driver.refresh()