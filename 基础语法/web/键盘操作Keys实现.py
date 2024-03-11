
# -*- coding: utf-8 -*-
# @Time :2020/8/2 18:55
# @Author : liufei
# @File :键盘操作.PY
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.taobao.com/")
driver.maximize_window()

#可以通过看Keys的源码来了解都支持什么键盘操作
# 使用 send_keys() 方法，与输入文本类似。
driver.find_element_by_id("key").send_keys("蒙牛") # 定位搜索框并输入内容
driver.find_element_by_id("key").send_keys(Keys.ENTER) # 发送键盘回车事件

# 除了上面的写法，如果你想传入组合键，比如 Ctrl+A， Ctrl+Shit+A：
driver.find_element_by_id("key").send_keys(Keys.CONTROL, 'a')
driver.find_element_by_id("key").send_keys(Keys.CONTROL, Keys.SHIFT, 'a')

'''
                                                        不容易理解的一些键
键名	说明
ADD	        +键
ARROW_DOWN	↓键
ARROW_LEFT	←键
ARROW_RIGHT	→键
ARROW_UP	↑键
CANCEL	    Cancel键，相当于ESCAPE(ESC)键
DECIMAL	    .键
DIVIDE	    /键
EQUALS	    =键
MULTIPLY	*键
NULL	    ''空键
PAUSE	    Pause键
SEMICOLON	;键
SEPARATOR	,键
SUBTRACT	-键
'''


