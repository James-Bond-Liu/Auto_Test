# -*- coding: utf-8 -*-
# @Time :2020/7/18 9:48
# @Author : liufei
# @File :cgadsfg.PY

import re
'''
re模块下的match()和search()方法区别：
match()只匹配string的开始，它是从开始位置进行匹配的，如果string的开始位置不符合，pattern则失败
search()匹配整个string，直到找到第一个符合pattern的对象
注意：两个方法均是只匹配一次，若想在一个string中进行多次匹配pattern可以利用pattern循环
'''
#利用“(pattern1)(pattern2)”这种形式可以对pattern进行分组，从而获得某一组的字符串
m=re.search("(\d+)([a-z]{2,5})","1234abcd")
m=re.match("(\d+)([a-z]{2,5})","1234abcd")

#group分组，根据pattern表达式里面的括号进行分组，开始位置是 1 .
#group()和group(0)相同，都是获取整组pattern的匹配结果（全部字符）
print(m.group())
print(m.group(0))

#group(1),当group()中传入参数后，获取相应的子组的匹配结果
print(m.group(1))#返回第一组pattern的匹配结果
print(m.group(2))#返回第二组pattern的匹配结果
print(m.group(1,2))#返回第一组第二组pattern的匹配结果，并将结果存储在元组中
print(m.group(0,1,2))#返回整组、第一组、第二组pattern的匹配结果，并将结果存储在元组中

'''
re.findall(pattern, string),在字符串找到所有的匹配子字符串.
如果有分组, 则返回与分组匹配的字符串.
如果使用了不止一个分组, 返回的列表中, 每一项都是一个元组
'''
s = "abc1234fa67a89"
r = re.findall("\d+[a-z]+", s)
print(r)
r = re.findall("(\d+)[a-z]+", s)
print(r)
r = re.findall("(\d+)([a-z]+)", s)
print(r)
