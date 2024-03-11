# -*- coding: utf-8 -*-
# @Time :2020/8/1 20:24
# @Author : liufei
# @File :鼠标操作.PY

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(r'https://www.baidu.com/')
driver.maximize_window()
'''
一般的下拉列表(html中元素组成非select标签)操作方式
先让下拉列表显示出来，定位成功后再进行一些操作
'''
ele = driver.find_element_by_xpath("//div[@id='u1']//span[@id='s-usersetting-top']")
ac = ActionChains(driver)
ac.move_to_element(ele)
ac.perform()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()
'''
当下拉列表的html页面组成为select标签时，selenium提供了专门用于处理select/option的下拉框--Select类
不需要先让下拉列表显示出来再定位，Select标签下的下拉框列表可以直接进行定位
'''
#引入类Select
from selenium.webdriver.support.ui import Select

#找到Select元素
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH, ".....")))
select_ele = driver.find_element_by_xpath(".....")

#实例化select类
s = Select(select_ele)

#选择元素，即选择下拉列表值
#通过value属性的值定位元素
s.select_by_value('***')

#通过文本内容定位元素
s.select_by_visible_text("***")

#通过从索引定位元素，从“0”开始
s.select_by_index(2)