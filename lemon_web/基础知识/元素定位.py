# -*- coding: utf-8 -*-
# @Time :2020/10/14 20:32
# @Author : liufei
# @File :元素定位.PY

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/index.php?tn=monline_3_dg")
driver.maximize_window()
driver.get("http:www.taobao.com")

'''
selenium之css_selector定位汇总
'''
# 一：单一属性定位
# 1、通过标签名定位，单一属性定位
driver.find_element_by_css_selector('input')

# 2、通过id定位
driver.find_element_by_css_selector('#kw')

# 3、通过class 定位
driver.find_element_by_css_selector('.s_ipt')

# 4、其他属性定位
driver.find_element_by_css_selector('[name="wd"]')
driver.find_element_by_css_selector("[type='text']")

# 二：组合属性定位
# 1、id组合属性定位==‘#’
driver.find_element_by_css_selector("input#kw")

# 2、class组合属性定位==‘.’
driver.find_element_by_css_selector("input.s_ipt")

# 3、其他属性组合定位==‘标签名[属性名='属性值']’
driver.find_element_by_css_selector("input[name='wd']")

# 4、仅有属性名，没有值也可以==‘标签名[属性名]’
driver.find_element_by_css_selector("input[name]")

# 5、两个其他属性组合定位==‘标签名[属性名='属性值'][属性名='属性值']’
driver.find_element_by_css_selector("[name='wd'][autocomplete='off']")

# 6、模糊匹配属性值方法
# 1>属性值由多个空格隔开，匹配其中一个值的方法--~=
driver.find_element_by_css_selector("input[class~='btn']")

# 2>匹配属性值为字符串开头的方法--^=
driver.find_element_by_css_selector("input[class^='btn']")

# 3>匹配属性值字符串结尾的方法--$=
driver.find_element_by_css_selector("input[class$='s_btn']")

# 4>匹配被'_'分割的属性值的方法,如上图的class
driver.find_element_by_css_selector("input[class|='s']")  #要求精确填写的属性值

# 三：层级定位
# 1：E>F    E下面的F这个元素
driver.find_element_by_css_selector('from#fm>span>input')#id是form(class值为fm)下面的span下面的input

# 2：E:nth-child(n)  某个标签下面的子级，根据索引定位，从1开始
driver.find_element_by_css_selector('#u_sp > a:nth-child(1)')#id为u_sp的下面的第一个a标签。

# 3：E:nth-last-child(n)，如字面意思：倒数第几个标签
driver.find_element_by_css_selector('#u_sp > a:nth-child(3)')

# 4：E:first-child,第一个标签
driver.find_element_by_css_selector('#u_sp > a:first-child')

# 5：E:last-child,最后一个标签
driver.find_element_by_css_selector('#u_sp > a:last-child')

# 6：E:only-child,唯一的标签
driver.find_element_by_css_selector('#u_sp > a:only-child')