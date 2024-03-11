# -*- coding: utf-8 -*-
# @Time :2020/8/8 13:16
# @Author : liufei
# @File :login_data.PY

#正常登录
success_data = {"user": 13890453721, "password": "iphone12"}

#异常登录-手机号格式不正确(大于11位，小于11位，不在号码段，为空）
phone_data = [
    {"user": 1389045372123, "password": "iphone12", "check": "请输入正确手机号"},
    {"user": 13890453, "password": "iphone12", "check": "请输入正确手机号"},
    {"user": 111389045372, "password": "iphone12", "check": "请输入正确手机号"},
    {"user": "", "password": "iphone12", "check": "请输入手机号"},
    {"user": 1389045372123, "password": "", "check": "请输入密码"}
]

password_data = [
    {"user": 1389045372123, "password": "hone12", "check":""},
    {"user": 1389045372123, "password": "hone12", "check":""},
    {"user": 1389045372123, "password": "hone12", "check":""}
]

