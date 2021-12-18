# -*- coding: utf-8 -*-
# @Time :2021/5/15 15:06
# @Author : liufei
# @File :练习.PY

# from conf.global_data import GlobalData
# a = GlobalData()
# setattr(a, 'token', 'jsdjf')
# print(getattr(a, 'token'))

from configparser import ConfigParser
cf = ConfigParser()
cf.read('D:\Python_files\lemon_API\conf\liufei.ini')
cf.set('conf', 'token', '123')
cf.write(open('D:\Python_files\lemon_API\conf\liufei.ini', 'w'))
print(eval(cf.get('conf','token')).__class__)
