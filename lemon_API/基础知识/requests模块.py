# -*- coding: utf-8 -*-
# @Time :2020/6/10 19:07
# @Author : liufei
# @File :class_0610.PY

import requests
#                                         #GET请求
# url='https://www.ketangpai.cn/User/login.html'
# dictory={'phone':'15631128376','key':'www.950620.cn'}
# header={'User-Agent': 'Mozilla/5.0'}
# res=requests.get(url, dictory, headers=header)
# print(res.headers)#获取响应消息的响应头
# print("*"*50)
# print(res.status_code)#获取响应消息的状态码
# print("*"*50)
# print(res.text)#获取响应报文
# print("*"*50)
# print(res.request.headers)#通过响应消息来获取《请求头》
#
#                                                     # POST请求
# url='https://www.ketangpai.cn/User/login.html'
# data={'mobilephone':'156311276','password':'www.950620.com'}
# res=requests.post(url,data=data)
#
# #获取响应头
# print(res.headers)
# print('*'*50)
#
# #获取响应响应体中的cookie
# print(res.cookies)
# print('*'*50)
#
# #cookie中的内容是一种类字典的格式，可以通过字典[key]的方法来提取value
# print(res.cookies['SERVERID'])
# print('*'*50)
# print(res.cookies['PHPSESSID'])
# print('*'*50)
#
# #获取状态码
# print(res.status_code)
# print('*'*50)
#
# #获取响应报文的json字典格式
# print(res.json())
# print('*'*50)

                                            #session会话请求
s=requests.session()
'''一般是先登录获取登录后的cookie后，然后再充值'''
'''但是利用session进行会话请求后就不用获取登录的cookie了，登录/充值两个请求在一个会话上面，充值请求直接可以进行'''
login_res=s.get('login_url',params='login_data')
rechare_res=s.post('rechare_url','recharge_data')

                                                #老黄历接口
url='http://v.juhe.cn/laohuangli/d'
key={'key':'4895879cc6f3906a452edaa58b367f8c','date':'2020-06-13'}
r=requests.get(url,key)
print(r)
print('*'*50)
print(r.json())
print('*'*50)
print(r.status_code)
print('*'*50)
print(r.text)


