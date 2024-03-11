# -*- coding: utf-8 -*-
# @Time :2020/9/5 13:28
# @Author : liufei
# @File :混合应用-h5.PY

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time

'''混合应用=原生控件+html页面(class属性为webview)'''
desird_caps = {}
desird_caps['automationName'] = 'UiAutomator2'
desird_caps['platformName'] = 'Android'
desird_caps['platformVersion'] = '7.1'
desird_caps['deviceName'] = 'Android Emulator'
desird_caps['appPackage'] = 'com.lemon.lemonban'
desird_caps['appActivity'] = 'com.com.lemon.lemonban.activity.WelcomeActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)

loc1 = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全程班")')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc1))
driver.find_element_by_android_uiautomator(loc1[1]).click()

#等待webview元素出现，
loc2 = (MobileBy.CLASS_NAME, 'android.webkit.WebView')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((loc2)))
time.sleep(1)

#前提：代码可以识别webview,需要开启app的webview的debug属性
#context包括两种内容：原生控件， webview
#列出所有的上下文,存储在列表中
cons = driver.contexts

#切换至webview。
# 要确保chrome driver的版本和webview的版本(webview可以通过uc-devtools获得版本)相匹配，而且放在相对应的位置。
driver.switch_to.context(cons[-1])

#切换之后，当前的操作页面即为html页面（所有操作与selenium中相同）。
# 利用uc-devtools工具来识别html页面，定位元素 或者翻墙在 chrome://inspect/#devices中识别
#等待元素可见
loc3 = (MobileBy.XPATH, '//button[@class="bottom-btn buy"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc3))
driver.find_element_by_xpath(loc3[1]).click()
