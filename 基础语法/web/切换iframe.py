# -*- coding: utf-8 -*-
# @Time :2020/8/1 17:14
# @Author : liufei
# @File :切换iframe.PY

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.taobao.com/")
driver.maximize_window()

#方式一：切换frame页面
#frame方法传参数有三中方式，index,name,WebElement对象
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'5373f0e9')]"))
sleep(0.5)

driver.find_element_by_id("tb-beacon-aplus").click()

#方式二：切换iframe页面
#EC下的frame_to_be_available_and_switch_to_it()类，需要传入一个元组类型的locator参数（定位类型，定位表达式）
#利用元素判断条件来切换，且源码中已经切换到iframe页面，所以就不需要driver.switch_to.方法了。既显示等待了，也切换至新的html页面了
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[contains(@id,'5373f0e9')]")))
sleep(0.5)

#从新的HTML页面切换至默认的HTML页面
driver.switch_to.default_content()

#从一个html页面（iframe）切换至其上一级（父级）html（iframe）中
driver.switch_to.parent_frame()


