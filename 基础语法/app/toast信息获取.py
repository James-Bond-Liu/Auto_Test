# -*- coding: utf-8 -*-
# @Time :2020/9/3 19:49
# @Author : liufei
# @File :toast信息获取.PY

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desird_caps = {}
desird_caps['automationName'] = 'UiAutomator2'
desird_caps['platformName'] = 'Android'
desird_caps['platformVersion'] = '7.1'
desird_caps['deviceName'] = 'Android Emulator'
desird_caps['appPackage'] = 'com.lemon.lemonban'
desird_caps['appActivity'] = 'com.com.lemon.lemonban.activity.WelcomeActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)

#点击‘我的柠檬’
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ID, 'com.lemon.lemonban:id/navigation_my')))
driver.find_element_by_id('com.lemon.lemonban:id/navigation_my').click()
#点击‘我的头像’
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avator_layout')))
driver.find_element_by_id('com.lemon.lemonban:id/fragment_my_lemon_avator_layout').click()
#不输入用户名密码直接点击登录按钮，一般会弹出“手机号码或密码为空”的提示框，即toast信息
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ID, 'com.lemon.lemonban:id/btn_login')))
driver.find_element_by_id('com.lemon.lemonban:id/btn_login').click()

#XPATH定位，匹配toast提示信息的文本内容
#注意在appium中，text属于元素的属性（需要加上@符号），而在selenium中text仅仅是一个文本不是属性（不需要加@符号）
loc = (MobileBy.XPATH, '//*[contains(@text, "手机号码或密码")]')

#元素等待，注意toast信息提取时，元素等待只能使用presence_of_element_located()
WebDriverWait(driver, 10, 0.01).until(EC.presence_of_element_located(loc))
try:
    text = driver.find_element_by_xpath('//*[contains(@text, "手机号码或密码")]').text()
    print(text)
except:
    print('没有找到匹配的toast信息')
