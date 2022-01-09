# -*- coding: utf-8 -*-
# @Time :2020/8/10 20:32
# @Author : liufei
# @File :basepage.PY

import datetime
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lemon_item.Web.Common import dir_config
from lemon_item.Web.Common.logging import Logging

#封装基本函数-执行日志，异常处理，失败截图
#所有页面的公共操作部分(不是业务层面，跟业务无关)

class BasePage():
    logging = Logging.do_logging()
    def __init__(self, driver):
        self.driver = driver

    #等待元素可见
    def wait_eleVisable(self, locator, time=30, poll_frequency=0.5, doc=""):
        '''
        :param locator:元素定位，元组形式（元素定位类型，定位表达式）
        :param time:最长等待时间
        :param poll_frequency:巡查周期间隔
        :param doc:模块名-页面名-操作名
        :return:None
        '''
        self.logging.info('等待元素{0}可见'.format(locator))
        try:
            start_time = datetime.datetime.now()    #开始元素等待的时间
            WebDriverWait(self.driver, time, poll_frequency).until(EC.visibility_of_element_located(locator))
            end_time = datetime.datetime.now()    #结束元素等待的时间
            wait_time = (end_time-start_time).seconds
            self.logging.info('{0}元素等待结束，等待时间{1}'.format(locator, wait_time))   #求一个差值，表示等待了多少秒
        except:
            self.logging.exception("等待元素可见失败！！")
            self.save_screenShoot(doc)  #截图
            raise   #抛出异常

    #d等待元素存在
    def wait_elePressence(self, locator, time=20, doc=''):
        self.logging.info('等待元素{0}可见'.format(locator))
        try:
            start_time = datetime.datetime.now()
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
            end_time = datetime.datetime.now()
            wait_time = (end_time - start_time).seconds
            self.logging.info('{0}元素等待元素存在结束，等待时间{1}'.format(locator, wait_time))
        except:
            self.logging.exception('等待元素存在失败')
            self.save_screenShoot(doc)
            raise

    #查找元素
    def get_element(self, locator, doc=""):
        self.logging.info('查找元素{0}'.format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            self.logging.exception("查找元素可见失败！！")
            self.save_screenShoot(doc)  # 截图
            raise  # 抛出异常

    #查找符合条件的所有元素（组元素）
    def get_elements(self, locator, doc=""):
        self.logging.info('查找符合表达式{0}的所有元素'.format(locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            self.logging.exception("查找符合表达式{0}的所有元素失败！！".format(locator))
            self.save_screenShoot(doc)  # 截图
            raise  # 抛出异常

    #点击操作
    def click_element(self, locator, doc=""):
        ele = self.get_element(locator, doc)    #找元素
        self.logging.info('{0}点击元素{1}'.format(doc, locator))
        try:
            ele.click()     #元素操作
        except:
            self.logging.exception("元素点击失败！！")
            self.save_screenShoot(doc)  # 截图
            raise  # 抛出异常

    #输入操作
    def input_text(self, locator, text, doc=""):
        ele = self.get_element(locator, doc)  # 找元素
        self.logging.info("{0}内的{1}输入内容{2}".format(doc, locator, text))
        try:
            ele.send_keys(text)     #输入操作
        except:
            self.logging.exception("元素输入文本操作失败！！")
            self.save_screenShoot(doc)  # 截图
            raise  # 抛出异常


    #获取元素文本内容
    def get_eleText(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        self.logging.info("{0}获取元素{1}的文本内容".format(doc, locator))
        try:
            return ele.text()  #返回获取的文本
        except:
            self.logging.exception("获取元素文本操作失败！！")
            self.save_screenShoot(doc)  # 截图
            raise  # 抛出异常

    #获取元素属性
    def get_element_attribute(self, locator, doc, attr_name):
        ele = self.get_element(locator, doc)
        self.logging.info("{0}获取元素{1}的属性".format(doc, locator))
        try:
            return ele.get_attribute(attr_name)  # 输入操作
        except:
            self.logging.exception("获取元素属性操作失败！！")
            self.save_screenShoot(doc)  # 截图
            raise  # 抛出异常

    #元素存在返回True,不存在返回False
    def is_eleExist(self, locator, time=10, doc=""):
        self.logging.info("在页面{0}中是否存在元素：{1}".format(doc, locator))
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
            self.logging.info('{0}元素等待元素存在结束'.format(locator))
            return True
        except:
            self.logging.info("在页面{0}中不存在元素：{1}".format(doc, locator))
            self.save_screenShoot(doc)  # 截图
            return False

    #alert处理
    def alert_action(self, action='accept'):
        pass

    #iframe切换
    def switch_iframe(self):
        pass

    #上传操作
    def upload_file(self):
        pass

    #截图操作
    def save_screenShoot(self, doc):
        #图片名称；模块名-页面名-操作名-年-月-日-时分秒.png
        file_path = dir_config.screenshoot_dir+"\{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H%-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(file_path)
            self.logging.info("截屏成功，文件路径为{}".format(file_path))
        except:
            self.logging.exception('截屏失败')


    #滚动条处理
    #窗口切换
