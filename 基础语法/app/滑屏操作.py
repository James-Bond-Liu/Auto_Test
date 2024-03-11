# -*- coding: utf-8 -*-
# @Time :2020/8/31 20:45
# @Author : liufei
# @File :滑屏操作.PY

from appium import webdriver

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

#左右滑动
size = driver.get_window_size()     #get_window_size()--返回窗口的宽，高
start_x1 = size['width'] * 0.9
start_y1 = size['height'] * 0.5
end_x1 = size['width'] * 0.1
end_y1 = size['height'] * 0.5
#从右向左滑
#swipe()滑动接口，swipe(起始X，起始Y，结束X，结束Y，滑动屏幕所用的时间n毫秒)
driver.swipe(start_x1, start_y1, end_x1, end_y1, 200)
#从左向右滑
driver.swipe(end_x1, end_y1, start_x1, start_y1, 200)

#上下滑动
start_x2 = size['width'] * 0.5
start_y2 = size['height'] * 0.9
end_x2 = size['width'] * 0.5
end_y2 = size['height'] * 0.1
#向上滑动
driver.swipe(start_x2, start_y2, end_x2, end_y2)
#向下滑动
driver.swipe(start_x2, end_y2, end_x2, start_y2)
