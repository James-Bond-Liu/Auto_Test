# -*- coding: utf-8 -*-
# @Time :2020/6/26 15:56
# @Author : liufei
# @File :ten.PY

dict={'zhangshan':14,'lisi':5,'wangwu':3,'zhouliu':54}

for s in dict:#遍历字典中的key
    print(s)
print('*'*30)

for x in dict.keys():#遍历字典中的key
    print(x)
print('*'*30)

for n in dict.values():#遍历字典中的value
    print(n)

for i, x in dict.items():#遍历字典中的key,value键值对，每一对key:value存储在一个元组中
    print(i)
    print(x)



