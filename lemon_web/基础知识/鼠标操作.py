# -*- coding: utf-8 -*-
# @Time :2020/8/1 20:24
# @Author : liufei
# @File :鼠标操作.PY
'''
                                                                鼠标操作列举
def click(self, on_element=None)  鼠标左键单击

def click_and_hold(self, on_element=None)  鼠标左键按键，不释放

def context_click(self, on_element=None)  鼠标右击

def double_click(self, on_element=None)  鼠标左键双击

def drag_and_drop(self, source, target)  鼠标拖曳动作,将指定元素位置拖曳到目标元素位置，来移动元素

def drag_and_drop_by_offset(self, source, xoffset, yoffset)  鼠标拖曳动作，将指定元素按沿x、y方向拖曳指定距离来移动元素

def move_by_offset(self, xoffset, yoffset)  将鼠标光标沿x、y方向移动指定距离，来实现鼠标的移动

def move_to_element(self, to_element)  将鼠标光标移动到指定的元素上

def move_to_element_with_offset(self, to_element, xoffset, yoffset)  将鼠标光标移动到指定的元素相对元素左上角位置偏移（xoffset、yoffset）的位置

def release(self, on_element=None)  释放鼠标,与click_and_hold函数配对使用

def key_down(self, value, element=None)  按下指定的键盘按键

def key_up(self, value, element=None)  释放已按下的键盘按键（与key_down配套使用）

                                                    键盘操作
def send_keys(self, *keys_to_send)  键盘输入

def send_keys_to_element(self, element, *keys_to_send)  给指定元素（可输入元素）进行键盘输入

                                                    其他
def perform(self)  执行所有存储的动作

def reset_actions(self)  清空所有存储的动作

def pause(self, seconds)  在指定的时间内暂定所有的输入
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(r'https://www.baidu.com/')
driver.maximize_window()
'''
首先把当前的driver对象赋予给ActionsChains类，让ActionsChains知道是哪个driver实例在操作鼠标，
其次再传入需要被定位元素位置，让鼠标对此元素执行click操作，
当传入一个web element对象时则在相应位置进行鼠标操作，不传入参数则在鼠标当前位置进行鼠标操作
最后借助perform执行上面规划好的动作链
例如：ActionChains(driver).context_click(right_click).perform()
'''

#定位鼠标操作的元素,生成一个WebElement对象
ele = driver.find_element_by_xpath("//div[@id='u1']//span[@id='s-usersetting-top']")

#实例化ActionChains类
ac = ActionChains(driver)

#将鼠标操作添加至actions列表中，鼠标动作被存储在列表中
#move_to_element()源码中的no_element参数是一个WebElement对象，
#当传入一个web element对象时则在相应位置进行鼠标操作，不传入参数则在鼠标当前位置进行鼠标操作
ac.move_to_element(ele)

#调用perform()方法来执行actions列表中鼠标操作
ac.perform()

#以上内容可以写成一行代码
# ActionChains(driver).move_to_element(ele).perform()

#显性等待目标元素出现
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="高级搜索"]')))

#选择下拉列表中的高级搜索
driver.find_element_by_xpath('//a[text()="高级搜索"]').click() #当传入一个web element对象时则在相应位置进行鼠标操作，不传入参数则在鼠标当前位置进行鼠标操作
