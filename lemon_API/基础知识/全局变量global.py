# -*- coding: utf-8 -*-
# @Time :2020/5/31 12:59
# @Author : liufei
# @File :class_0531.PY

#全局变量
a=1
def num_fun(b):
    global a
    a=5
    x=a+b
    print(x)
num_fun(10)
print(a)

