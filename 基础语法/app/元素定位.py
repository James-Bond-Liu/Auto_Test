# -*- coding: utf-8 -*-
# @Time :2020/8/30 19:37
# @Author : liufei
# @File :元素定位.PY

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desird_caps = {}
#appium服务器初始化
#平台类型
desird_caps['platformName'] = 'Android'
#平台版本号
desird_caps['platformVersion'] = '7.1'
#设备名称
desird_caps['deviceName'] = 'Android Emulator'
#app包名
desird_caps['appPackage'] = 'com.wandoujia.phoenix2'
#app入口activitiy
desird_caps['appActivity'] = 'com.pp.assistant.activity.PPMainActivity'
#连接appium server.
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)

'''
app中的元素定位类型既有自己特殊的定位类型(accessibility_id、android_uiautomator等)
又继承了web中selenium中的元素定位类型(tag_name、LINK_TEXT等)
'''
#元素定位，返回一个webelement对象
#通过resource-id定位元素
driver.find_element_by_id('com.lemon.lemonban:id/navigation_tiku')
#通过class定位元素
driver.find_element_by_class_name('android.widget.FrameLayout')
#通过content-desc定位元素
driver.find_element_by_accessibility_id('******')
#通过AndroidUiAutomator定位元素
driver.find_element_by_android_uiautomator('new UiSelector().text("柠檬社区")')


