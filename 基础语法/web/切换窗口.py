# -*- coding: utf-8 -*-
# @Time :2020/8/1 17:48
# @Author : liufei
# @File :切换窗口.PY

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(30)

#定位到百度首页的输入框中，输入搜索内容
driver.find_element_by_id('kw').send_keys('柠檬班')

#点击搜索
# driver.find_element_by_id('su').click()#利用鼠标进行点击
driver.find_element_by_id('su').send_keys(Keys.ENTER)#利用快捷键，ENTER进行搜索

#显示等待元素出现
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id=2]//h3[contains(@class,'c-gap-bo')]//a")))

#获取所有窗口的句柄,存储在一个列表中
#如若利用new_window_is_opened类，进行判断，必须在窗口总数发生变化之前获取局柄总数
handles = driver.window_handles
print(handles)

#打开一个新的窗口,引起窗口数量变化
driver.find_element_by_xpath("//*[@id=2]//h3[contains(@class,'c-gap-bo')]//a").click()

sleep(1)
#显示等待新窗口出现
# new_window_is_opened类传入的参数是，新窗口未打开之前的句柄总数
WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))

#重新获取一次窗口句柄总数
#因为之前的句柄总数是未打开新窗口之气的，所以需要重新获取一次句柄，再利用列表取值进行切换窗口
handles2 = driver.window_handles

#切换窗口
driver.switch_to.window(handles2[-1])

#显示等待元素出现
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"tab_picture")))

#定位新窗口下的元素
driver.find_element_by_id("tab_picture").click()

#获取当前窗口的句柄
handle = driver.current_window_handle
print(handle)


