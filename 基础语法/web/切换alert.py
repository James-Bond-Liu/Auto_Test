# -*- coding: utf-8 -*-
# @Time :2020/8/1 19:17
# @Author : liufei
# @File :切换alert.PY

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''alert弹出框并不是html页面元素。弹出框一共分两种，一种html页面弹出框，另一种windows弹出框(比如alert出框)，'''
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()

#显性等待alert弹框出现，alert_is_present不用传任何参数，注意看源码
WebDriverWait(driver, 10).until(EC.alert_is_present())

#切换至alert弹框
alert = driver.switch_to.alert

#获取弹框的内容
alert.text

#往弹框填写内容
alert.send_keys("哈哈")

#关闭弹出框，以下两种均可关闭弹框s
alert.accept()#相当于点击“是”
alert.dismiss()#相当于点击“否”
