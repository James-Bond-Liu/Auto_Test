# -*- coding: utf-8 -*-
# @Time :2020/10/24 16:07
# @Author : liufei
# @File :sdgd.PY
#通过AndroidUiAutomator定位元素
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desird_caps = {}
#appium服务器初始化
desird_caps['platformName'] = 'Android'
desird_caps['platformVersion'] = '7.1'
desird_caps['deviceName'] = 'Android Emulator'
desird_caps['appPackage'] = 'com.wandoujia.phoenix2'
desird_caps['appActivity'] = 'com.pp.assistant.activity.PPMainActivity'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desird_caps)
driver.find_element_by_android_uiautomator('new UiSelector().text("柠檬社区")')
'''
UiSelector类中的方法，调用举例：new UiSelector().text("柠檬社区")
`checkable(boolean val)`设置搜索条件以匹配可检查的小部件。
`checked(boolean val)`设置搜索条件以匹配当前选中的小部件（通常用于复选框）。
`childSelector(UiSelector selector)`向此选择器添加子UiSelector条件。
`className(String className)`设置搜索条件以匹配小部件的class属性（例如，“ android.widget.Button”）。
`className(Class<T> type)`设置搜索条件以匹配小部件的class属性（例如，“ android.widget.Button”）。
`classNameMatches(String regex)`使用正则表达式设置搜索条件以匹配小部件的class属性。
`clickable(boolean val)`设置搜索条件以匹配可单击的小部件。
`description(String desc)`设置搜索条件以匹配窗口小部件的content-description属性
`descriptionContains(String desc)`设置搜索条件以匹配窗口小部件的content-description属性。
`descriptionMatches(String regex)`设置搜索条件以匹配窗口小部件的content-description属性。
`descriptionStartsWith(String desc)`设置搜索条件以匹配窗口小部件的content-description属性。
`enabled(boolean val)`设置搜索条件以匹配已启用的窗口小部件。
`focusable(boolean val)`设置搜索条件以匹配可聚焦的小部件。
`focused(boolean val)`设置搜索条件以匹配具有焦点的窗口小部件。
`fromParent(UiSelector selector)`向此选择器添加子UiSelector条件，该条件用于从父窗口小部件开始搜索。
`index(int index)`设置搜索条件以通过窗口小部件在布局层次结构中的节点索引来匹配窗口小部件。
`instance(int instance)`设置搜索条件以通过其实例号匹配窗口小部件。
`longClickable(boolean val)`设置搜索条件以匹配可长时间单击的窗口小部件。
`packageName(String name)`设置搜索条件以匹配包含窗口小部件的应用程序的程序包名称。
`packageNameMatches(String regex)`设置搜索条件以匹配包含窗口小部件的应用程序的程序包名称。
`resourceId(String id)`设置搜索条件以匹配给定的资源ID。
`resourceIdMatches(String regex)`使用正则表达式设置搜索条件以匹配窗口小部件的资源ID。
`scrollable(boolean val)`设置搜索条件以匹配可滚动的小部件。
`selected(boolean val)`设置搜索条件以匹配当前选定的小部件。
`text(String text)`设置搜索条件以匹配窗口小部件中显示的可见文本（例如，用于启动应用程序的文本标签）。
`textContains(String text)`设置搜索条件以匹配窗口小部件中的可见文本，其中可见文本必须在输入参数中包含字符串。
`textMatches(String regex)`使用正则表达式设置搜索条件以匹配显示在布局元素中的可见文本。
`textStartsWith(String text)`设置搜索条件以匹配以text参数为前缀的小部件中的可见文本。
'''