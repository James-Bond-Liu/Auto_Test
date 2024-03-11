# -*- coding: utf-8 -*-
# @Time :2020/6/25 16:22
# @Author : liufei
# @File :http_request.PY

import requests
from framework.api.tools.output_log import OutPutLog
logger=OutPutLog().out_log()
class HttpRequest():
    @staticmethod
    def http_request(url,data,http_method,cookies=None):
        try:
            if http_method.upper()=='GET':
                res=requests.get(url,data,cookies=cookies)
            elif http_method.upper()=='POST':
                res=requests.post(url,data,cookies=cookies)
            else:
                logger.error('输入的请求方法不正确')
        except Exception as e:
            logger.error("请求出错了{0}".format(e))
            raise e
        return res
