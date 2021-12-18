# -*- coding: utf-8 -*-
# @Time :2020/8/1 15:22
# @Author : liufei
# @File :元素定位.PY

from selenium import webdriver
from time import sleep
#下面是利用显性等待时所需要的模块
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(r'https://www.baidu.com/')
driver.maximize_window()
#强制等待
sleep(2)

#隐形等待，作用于全局
driver.implicitly_wait(2)

#点击登录按钮，弹出登录页面
ele1 = driver.find_element_by_xpath("//a[contains(@class,'s-top-login-bt')]") #生成一个WebElement对象
ele1.click()

#显性等待元素定位
# visibility_of_element_located()类需要传入一个locator参数，由（定位类型，定位表达式）构成的元组
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[text()='用户名登录']")))

#点击用户名密码登录
driver.find_element_by_xpath("//p[text()='用户名登录']").click()

#退出浏览器
driver.quit()

