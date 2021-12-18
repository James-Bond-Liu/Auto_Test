# -*- coding: utf-8 -*-
# @Time :2020/7/5 18:43
# @Author : liufei
# @File :do_zip.PY

s1=[1,2,3]
s2=['one','two','three']

#可以理解为先压缩，然后再解压为目标类型。
print(list(zip(s1,s2)))  #[(1, 'one'), (2, 'two'), (3, 'three')]
print(dict(zip(s1,s2)))  #{1: 'one', 2: 'two', 3: 'three'}