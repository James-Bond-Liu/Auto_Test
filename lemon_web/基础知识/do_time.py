# -*- coding: utf-8 -*-
# @Time :2020/7/25 23:17
# @Author : liufei
# @File :do_time.PY

import datetime
from time import sleep

a=datetime.datetime.now()
print(a)
sleep(2)

b=datetime.datetime.now()
print(b)
print((b-a).seconds)

c=datetime.date.today()
print(c)