# -*- coding: utf-8 -*-
# @Time :2020/8/29 15:27
# @Author : liufei
# @File :demo.PY

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

#appium服务器初始化
desird_caps = {}
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
1、运行代码之前appium server启动成功，处于监听状态
2、模拟器/真机必须能够被电脑识别（adb devices）。
'''

#元素定位，返回一个webelement对象
#resource-id
driver.find_element_by_id('com.lemon.lemonban:id/navigation_tiku')
#class
driver.find_element_by_class_name('android.widget.FrameLayout')
#content-desc
driver.find_element_by_accessibility_id('******')
#AndroidUiAutomator
driver.find_element_by_android_uiautomator('new UiSelector().text("柠檬社区")')
