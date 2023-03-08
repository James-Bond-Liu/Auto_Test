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
方法	        说明
dumps()	    将Python对象编码成json字符串
loads()	    解码json数据，返回python对象
dump()	    将python对象编码成json数据并写入json文件中
load()	    从json文件中读取数据并解码为Python对象
'''

import json

'''字典转化为JSON并写入'''
# 创建python对象-字典
info_dict = {'name': 'Joe', 'age': 20, 'job': 'driver'}  # <class 'dict'>
print(type(info_dict))

# 将python对象转化为json字符串
info_json1=json.dumps(info_dict)  # {"name": "Joe", "age": 20, "job": "driver"} <class 'str'>

# 将json字符串转化为python对象
info_json2=json.loads(info_json1)  # {'name': 'Joe', 'age': 20, 'job': 'driver'} <class 'dict'>
print(info_json2)

# # 显示数据类型
# print(type(info_json1))
# f = open('info.json', 'w')
# f.write(info_json1)
#
# '''读取JSON文件，并转化为字典'''
# # JSON到字典转化
# f2 = open('info.json', 'r')
# info_data = json.load(f2)
# print(info_data)
# # 显示数据类型
# print(type(info_data))
