 # -*- coding: utf-8 -*-
# @Time :2020/6/13 10:26
# @Author : liufei
# @File :http_request.PY

import requests
class HttpRequest():
    def http_request(self,url,method,data,cookies=None):
        global res
        if method.lower()=='get':
            res = requests.get(url, data,cookies=cookies,verify=False)
        elif method.lower()=='post':
            res = requests.post(url,data,cookies=cookies,verify=False)
        return res
if __name__ == '__main__':
    # 登录请求
    url='http://ip:8080/futureloan/mvc/api/member/login'
    data={'name':'15631128476','passwd':'www.950620.cn'}
    res=HttpRequest().http_request(url,'get',data)
    print('登录结果',res.json())

    # 充值请求
    recharge_url='http://ip:8080/futureloan/mvc/api/member/recharge'
    recharge_data={'name':'15631128476','passwd':'www.950620.cn'}
    recharge_res=HttpRequest().http_request(recharge_url,'post',recharge_data,cookies=res.cookies)
    print('充值结果',recharge_res.json())
