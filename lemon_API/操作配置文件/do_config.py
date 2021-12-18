# -*- coding: utf-8 -*-
# @Time :2020/6/21 15:04
# @Author : liufei
# @File :ejfdilj.PY

import configparser
#数据类型，无论是数字还是列表等数据类型，一旦进入配置文件就全部转换成字符串。
#可以利用eval()函数将格式转化成原本的数据格式

cf=configparser.ConfigParser()
cf.read('case.config',encoding='utf-8') #打开文件
res1=cf.get('MODE','mode') #提取数据
print(res1)
print(cf.sections()) #提取配置文件中所有的标签
print(cf.items('PYTHON11')) #提取配置文件中PYTHON11标签下的所有的option 和 value
print(type(eval(cf.get('PYTHON11','name'))))

