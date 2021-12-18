# -*- coding: utf-8 -*-
# @Time :2020/7/4 20:08
# @Author : liufei
# @File :nine.PY

def bulid(first,last,**s):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in s.items():
        profile[key]=value
    return profile
k={'loaction':'princetion','field':'physics'}
'''
k 等价于，"loaction"="printcetion","field"="physics"
'''
user_profile=bulid('albert','einstein',**k) #"**变量名" 可以直接传入字典从而代替一个一个的传入关键字参数
print(user_profile)