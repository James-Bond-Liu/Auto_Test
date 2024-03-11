# -*- coding: utf-8 -*-
# @Time :2020/8/1 14:36
# @Author : liufei
# @File :打开浏览器.PY

from selenium import webdriver
from time import sleep

#生成一个driver对象,启动浏览器，开启与Chrome浏览器的会话
driver=webdriver.Chrome()
#访问网址
driver.get(r'https://www.baidu.com/')
#窗口最大化
driver.maximize_window()
#设置窗口大小
driver.set_window_size(200,300)
#强制等待
sleep(2)
driver.get('http://www.taobao.com')
sleep(2)
#回退至上一页面
driver.back()
sleep(2)
#前进至下一页面
driver.forward()
sleep(2)
#刷新
driver.refresh()
#获取标题，即浏览器窗口内的文本
print(driver.title)
#获取浏览器现在的网址
print(driver.current_url)
#获取窗口句柄
print(driver.current_window_handle)
'''
下面的quit()和close()方法要注意先后顺序，应该是先关闭窗口再关闭浏览器进程
'''
#关闭浏览器上的窗口
driver.close()
#关闭浏览器，并杀掉进程
driver.quit()


