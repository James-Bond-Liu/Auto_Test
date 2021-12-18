# -*- coding: utf-8 -*-
# @Time :2020/6/21 16:18
# @Author : liufei
# @File :read_config.PY

import configparser

class ReadConfig():
    def read_config(self,filename,section,option):
        cf=configparser.ConfigParser()
        cf.read(filename,encoding='utf-8') #打开文件
        res=cf.get(section,option) #提取数据
        return res

if __name__ == '__main__':
    print(ReadConfig().read_config('case.config', 'MODE', 'mode'))