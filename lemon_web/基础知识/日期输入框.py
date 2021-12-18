# -*- coding: utf-8 -*-
# @Time :2020/8/2 19:59
# @Author : liufei
# @File :日期输入框.PY

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
'''
日期输入框的input标签是readonly属性，然后又不想在弹出框中选择具体日期时，可以通过利用DOM更改元素的属性，使readonly的值由ture变为false
然后就可以直接编辑输入日期了。
'''
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
driver.maximize_window()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='train_date']")))

#利用JavaScript(DOM对象)来修改readOnly属性的值，将readOnly的值变为false后，便可以进行编辑了
#或者也可以利用JavaScript(DOM对象)来移除readOnly属性，然后就可以进行编辑了
js = 'var ele = document.getElementById("train_date");ele.readOnly = false;ele.value = "2020-09-12";'
driver.execute_script(js)

driver.find_element_by_link_text('查    询').click()
