# -*- coding: utf-8 -*-
# @Time :2020/9/2 20:32
# @Author : liufei
# @File :触屏操作.PY

'''
触屏操作需要用到TouchAction类（等同于selenium中ActionChains类）参考源码
短按--press
长按--longPress
点击--tap
移动到--move_to
等待--wait
释放--release
执行--perform
取消--cancel
注意：1、press、longPress一般和wait、release结合起来使用 2、一般情况下传参既可以传坐标，也可以传元素（element对象）
'''
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
desird_caps = {}
desird_caps['platformName'] = 'Android'
desird_caps['platformVersion'] = '7.1'
desird_caps['deviceName'] = 'Android Emulator'
desird_caps['appPackage'] = 'com.wandoujia.phoenix2'
desird_caps['appActivity'] = 'com.pp.assistant.activity.PPMainActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)

'''以九宫格解锁为例'''
#定位到待触屏的元素,返回一个element对象
ele = driver.find_element_by_id('*****')

#获取元素的尺寸,以字典的形式返回size={'height':xx,'width':xx}
size = ele.size

#均分步长，高宽一样长
step = size/6   #python中的除法返回的是一个整数。

#获取元素的起点坐标(左上角),以字典的形式返回，ori={'x':*, 'y':*}
ori = ele.location

point1 = (ori['x']+step, ori['y']+step)
point2 = (point1[0]+step*2, point1[1])      #相对于point1X轴增加2step
point3 = (point2[0]+step*2, point2[1])      #相对于point2X轴增加2step
point4 = (point3[0]-step*2, point3[1]+step*2)       #相对于point2X轴减少2step，Y轴增加2step
point5 = (point4[0], point4[1]+step*2)      #相对于point3Y轴增加2step

TouchAction(driver).press(x=point1[0], y=point1[1]).wait(200).\
    move_to(x=point2[0], y=point2[1]).wait(200).\
    move_to(x=point3[0], y=point3[1]).wait(200).\
    move_to(x=point4[0], y=point4[1]).wait(200).\
    move_to(x=point5[0], y=point5[1]).wait(200).\
    release().perform()








