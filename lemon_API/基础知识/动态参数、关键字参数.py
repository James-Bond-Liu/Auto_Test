# -*- coding: utf-8 -*-
# @Time :2020/10/4 20:52
# @Author : liufei
# @File :动态参数、关键字参数.PY

# #动态参数
# def add(*args):
#     print("你的汉堡有以下这些材料组成")
#     print(*args)
# add("鸡腿","生菜","培根")
#
# def add(k,*args):
#     print("你的汉堡有以下这些材料组成")
#     print(k,end=" ") #print()语句默认打印一行后添加换行操作。当有end=''时，末尾不换行，末尾是一个空字符。
#     print(*args)
# add("鸡腿","生菜","培根")
#
# #参数位置错误示范：
# def add(*args,k):#*args动态阐述是贪婪的，可以存储无穷多的实参，k不会收到任何实参，然后报错
#     print("你的汉堡有以下这些材料组成")
#     print(k)
#     print(*args)
# add("鸡腿","生菜","培根")

def add(*args,**kwargs): # **kwargs是关键字参数，是以key=value这种形式输入实参的
    print("你的汉堡有以下这些材料组成", end='')
    print(args)
    print(kwargs)

add("鸡腿","生菜","培根", s="面包")
