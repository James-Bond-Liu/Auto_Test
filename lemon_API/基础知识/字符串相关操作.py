# -*- coding: utf-8 -*-
# @Time :2020/5/27 19:20
# @Author : liufei
# @File :class_number.PY
import hashlib

b=0.45
print(type(b))
print(type(str(b))) #数据类型强制转换

a=True
print(type(a)) #布尔值

s="hello!"
print(len(s)) #统计字符串元素个数
print(s[0],s[5])
print(s[-1],s[-6])
print(s[1:4:2]) #字符串的切片
print(s[::-1]) #字符串的倒序输出
x=s.split("e") #字符串的切割
c=s.split("l",1) #字符串的切割，并指定次数
d=s.replace("e","@") #字符串的替换
f=s.replace("l","@",1) #字符串的替换，并指定替换次数
h=s+"world"
print(s,"world") #生成“s world”中间有空格
print(s+"world") #字符串的拼接，中间无空格。“sworld”

ss=" hello! "
g=ss.strip()#去除首尾的空格字符。还有rstrip,lstrip,该函数只作用于首尾
# 字符串加密 hashlib,注意需要先对加密的字符串进行编码转换，否则会报错
md = hashlib.md5()
s = 'Ltk123456'
md.update(s.encode(encoding='utf-8'))  # 对字符串进行编码转换
md.hexdigest()   # 对字符串进行加密, ab3a7e4cf5f8d34673809b7c1068e496


# 格式化输出字符串
#方法一 format
age=18
name="liufei"
print("2020年的{}，今年已经{}岁了".format(name,age))
print("2020年的{1}，今年已经{0}岁了".format(name,age))
#format 格式化输出简写方式
print(f"2020年的{name}， 今年已经{age}岁了")

#方法二 %
#%s,可以用来存放任何类型数据，%d,用来存放整形数据，如果存放浮点数，则会被强制转化成整型，
# 造成数据的不准不精确，%f,用来存放浮点数（%.3f,表示保留三位小数）
xingming="樱桃"
jiage=25
price=23.5
print("2020年的%s，今年已经%d元一斤了,也有可能降价到%.3f"%(xingming,jiage,price))

#字符串的映射： python 的translate函数，在使用translate方法之前，先利用maketrans（）方法制作一个映射表
s="qwertasdfgxcv"
intab="erfv"
outtab="1234"
trantab=s.maketrans(intab,outtab) #制作映射表
k=s.translate(trantab)
print(k)

#字符串大小写转换,调用swapcase()方法
a="kdjflsak"
print(a.swapcase())

