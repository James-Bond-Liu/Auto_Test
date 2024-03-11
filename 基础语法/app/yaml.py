# -*- coding: utf-8 -*-
# @Time :2020/9/9 21:40
# @Author : liufei
# @File :yaml.PY

import yaml

f = '''
 ---
 name: James
 age: 20
 ---
 name: Lily
 age: 19
 '''
y = yaml.load_all(f)
for data in y:
 print(data)
