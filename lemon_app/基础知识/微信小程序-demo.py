# -*- coding: utf-8 -*-
# @Time :2020/9/6 13:26
# @Author : liufei
# @File :微信小程序-demo.PY
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import os
import time

#启动appium时需要指定chromedriver.exe的目录。使用appium默认目录下的会报错
#在切换小程序webview时，会去匹配chrome内核的*的驱动。在切换完成之后，再打印所有
#所以指定一个非默认目录下面的chromedriver.exe（X5内核对应的版本），此问题就不会出现
#在appium.server上设置chromedriver的路径。

#appium服务器初始化
desird_caps = {}
#支持X5内核应用自动化配置
desird_caps['recreateChromeDriverSessions'] = True
#平台类型
desird_caps['platformName'] = 'Android'
#平台版本号
desird_caps['platformVersion'] = '7.1'
#设备名称
desird_caps['deviceName'] = 'Android Emulator'
#app包名
desird_caps['appPackage'] = 'com.tencent.mm'
#app入口activitiy
desird_caps['appActivity'] = 'com.tencent.mm.ui.LaucherUI'
#是否重置app应用(appium默认是重置的）
desird_caps['noReset'] = True
#ChromeOptions使用来定制启动选项的，因为微信、腾讯等应用有许多进程，在appium中切换context(上下文)识别webview的时候容易切错。
#所以为了避免这个问题，加上androidProcess: com.tencent.mm:toolsmp
desird_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:toolsmp'}
#涉及到html网页，如果用浏览器打开则指定浏览器名称，若仅仅是一个应用内的页面指定为空就好。
desird_caps['browserName'] = ''
#连接appium server.
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)

time.sleep(5)
#点击发现
driver.find_element_by_android_uiautomator('new UiSelector().text(\"发现\")').click()
#点击发现里面的搜一搜
driver.find_element_by_android_uiautomator('new UiSelector().text(\"搜一搜\")').click()
#等待搜索框出现
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, 'com.tencent.mm:id/jd')))
#点击搜索框
driver.find_element_by_id('com.tencent.mm:id/jd').click()
time.sleep(5)
#点击历史记录中的柠檬班软件测试（采用adb命令的方式点击坐标）
#原因：微信小程序界面是属于app的webview(一般发布的appwebview的等级不是debug所以不可见，无法利用元素定位进行点击操作）
os.system('adb shell input tap 281 205')
#点击柠檬班软件测试小程序
time.sleep(5)
os.system('adb shell input tap 364 470')
#等待小程序加载完成
time.sleep(10)
#获取所有的上下文
cons = driver.contexts
print('当前所有的上下文为：', cons)
#切换到小程序的webview
driver.switch_to.context('WEBVIEW_com.tencent.mm:toolsmp')
'''以下操作等同于web-selenium操作'''
#打印当前所有的窗口
hs = driver.window_handles
print('当前所有的窗口为：', hs)
#需要找到哪一个有柠檬班信息的窗口，然后在这个元素下面进行操作
#遍历所有的，找到当前页面所在的handle,若果pagesource中包含想要的元素，就是我要找的handle
#小程序的页面来回切换也需要：遍历所有的handles，切换到元素所在的handle
for handle in hs:
    driver.switch_to.window(handle)
    print('切换到{0}窗口'.format(handle))
    time.sleep(3)
    if driver.page_source.find('柠檬班') != -1:
        break
#点击老师
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.XPATH, '//*[@id="js-tab-bar"]')))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.XPATH, '//em[text()="歪歪"]')))
time.sleep(5)
#找到歪歪老师
ele = driver.find_element_by_xpath('//em[text()="歪歪"]')
#拖动到可见区域
driver.execute_script("arguments[0].scrollIntoViewIfNeed(true);", ele)


