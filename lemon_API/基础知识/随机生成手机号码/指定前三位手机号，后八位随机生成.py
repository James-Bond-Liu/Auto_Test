# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 18:39
# @Author  : Liu Fei
# @File    : 指定前三位手机号，后八位随机生成.py
# @Software: PyCharm
import random

phone_list = ['130', '131', '155', '158', '187', '186']
phone_number = random.choice(phone_list)+''.join(random.choice('0123456789') for i in range(8))
print(phone_number)
print(phone_number.__class__)
print(type(int(phone_number)))

