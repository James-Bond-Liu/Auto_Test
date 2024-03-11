# -*- coding: utf-8 -*-
# @Time :2021/3/1 20:44
# @Author : liufei
# @File :练习.PY

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("sudo pip install --upgrade " + dist.project_name, shell=True)  # 刘菲


def liu_fei(self):
    print("hello world")
