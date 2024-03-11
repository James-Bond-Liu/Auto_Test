# -*- coding: utf-8 -*-
# @Time :2020/8/2 19:02
# @Author : liufei
# @File :滚动条操作.PY

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

'''
滚动条不是html元素，它属于浏览器，它是利用Javascript来实现的
'''
# //a[contains(text(),"班的微博_微博")]
driver.find_element_by_id('kw').send_keys('柠檬班')
# driver.find_element_by_id('su').click()#利用鼠标进行点击
driver.find_element_by_id('su').send_keys(Keys.ENTER)#利用快捷键，ENTER进行搜索

#滚动条的处理
#1、找到要滚动到可视区域的元素
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"班的微博_微博")]')))
ele = driver.find_element_by_xpath('//a[contains(text(),"班的微博_微博")]')

#2、使用js进行滚动操作
#scrollIntoView()参数为Boolean型参数，传入false,移动WebElement对象至与当前窗口的底部对齐
driver.execute_script("arguments[0].scrollIntoView(false);", ele)
sleep(3)
#scrollIntoView()参数为Boolean型参数，传入true.默认值为true,移动WebElement对象至与当前窗口的顶部对齐
driver.execute_script("arguments[0].scrollIntoView();", ele)
sleep(3)
#移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(3)
#移动到页面顶部
driver.execute_script("window.scrollTo(0,0)")

#scrollIntoViewIfNeeded()方法也是用来将不在浏览器窗口的可见区域内的元素滚动到浏览器窗口的可见区域。
# 但如果该元素已经在浏览器窗口的可见区域内，则不会发生滚动。
#true为默认值，但不是滚动到顶部，而是让元素在可视区域中居中对齐；false时元素可能顶部或底部对齐，关键看元素靠哪边更近。
# 此方法是标准的Element.scrollIntoView()方法的专有变体。
driver.execute_script("arguments[0].scrollIntoViewIfNeed(true);", ele)
