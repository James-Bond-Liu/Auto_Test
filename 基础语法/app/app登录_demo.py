# -*- coding: utf-8 -*-
# @Time :2020/9/1 21:20
# @Author : liufei
# @File :app登录.PY

from appium import webdriver    #驱动
from appium.webdriver.common.mobileby import MobileBy   #元素等待类型，MobileBy同样继承了Selenium中的By

#元素显性等待和显性等待的条件，继承selenium中的
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#appium服务器初始化
desird_caps = {}
#平台类型
desird_caps['platformName'] = 'Android'
#平台版本号
desird_caps['platformVersion'] = '7.1'
#设备名称
desird_caps['deviceName'] = 'Android Emulator'
#app包名
desird_caps['appPackage'] = 'com.lemon.lemonban'
#app入口activitiy
desird_caps['appActivity'] = 'com.com.lemon.lemonban.activity.WelcomeActivity'
#连接appium server.
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)

#点击‘我的柠檬’
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ID, 'com.lemon.lemonban:id/navigation_my')))
driver.find_element_by_id('com.lemon.lemonban:id/navigation_my').click()
#点击‘我的头像’
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avator_layout')))
driver.find_element_by_id('com.lemon.lemonban:id/fragment_my_lemon_avator_layout').click()
#输入用户名密码
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ID, 'com.lemon.lemonban:id/et_mobile')))
driver.find_element_by_id('com.lemon.lemonban:id/et_mobile').send_keys('13489453452')
driver.find_element_by_id('com.lemon.lemonban:id/et_password').send_keys('123456')
driver.find_element_by_id('com.lemon.lemonban:id/btn_login').click()
