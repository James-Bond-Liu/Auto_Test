# -*- coding: utf-8 -*-
# @Time :2020/7/25 22:52
# @Author : liufei
# @File :class3.PY

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/index.php?tn=monline_3_dg")
driver.maximize_window()
driver.get("http:www.taobao.com")
driver.back()
time.sleep(10)
driver.forward()
driver.refresh()
print(driver.title)
print(driver.current_url)
print(driver.current_window_handle)
driver.quit()


