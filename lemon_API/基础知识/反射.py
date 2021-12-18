# -*- coding: utf-8 -*-
# @Time :2020/6/16 20:05
# @Author : liufei
# @File :class_01.PY

#反射

class GetData():
    cookie='888'

print(GetData.cookie)

#setattr()方法可以直接修改类里面的属性，set attribute  setattr(类名，属性名，新值)
setattr(GetData,'cookie','666')

#getattr()方法可以直接修改类里面的属性，get attribute  getattr(类名，属性名)
print(getattr(GetData,'cookie'))

#hasattr()方法用来判断类里面有没有相应的属性值hasattr(类名，属性名)
print(hasattr(GetData,'cookie'))

#delattr(GetData,'cookie')方法用来删除类下面相应的属性
delattr(GetData,'cookie')

print(hasattr(GetData,'cookie'))
print(GetData().cookie)