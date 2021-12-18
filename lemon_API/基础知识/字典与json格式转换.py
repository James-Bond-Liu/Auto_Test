# -*- coding: utf-8 -*-
# @Time :2021/5/12 20:54
# @Author : liufei
# @File :字典与json格式转换.PY

"""
json数据本质还是一个字符串类型数据
Json和字典区别总结：
    定义上：字典是一种数据结构；json是一种数据的表现形式，一种数据格式。
    写法上：字典中的键key，只要是hashable的数据类型即可；但是json的键key（属性名称），必须是用双引号引起来的字符串。
"""

'''
JSON在python中分别由list和dict组成。
在python中，JSON模块提供以下四个功能，
dumps、dump、loads、load。
其中dumps把数据类型转换成字符串
dump把数据类型转换成字符串并存储在文件中
loads把字符串转换成数据类型
load把文件打开从字符串转换成数据类型
'''
import json

'''字典转化为JSON并写入'''
# 创建字典
info_dict = {'name': 'Joe', 'age': 20, 'job': 'driver'}
# dumps 将数据转换成字符串
info_json1 = json.dumps(info_dict,sort_keys=False, indent=4, separators=(',', ': '))
# 将字符串数据转换成json格式
info_json2 = json.loads(info_json1)
# 显示数据类型
print(type(info_json1))
f = open('info.json', 'w')
f.write(info_json1)

'''读取JSON文件，并转化为字典'''
# JSON到字典转化
f2 = open('info.json', 'r')
info_data = json.load(f2)
print(info_data)
# 显示数据类型
print(type(info_data))
