# -*- coding: utf-8 -*-
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests
from common.out_log import OutLog

logger = OutLog().out_log()


class HttpRequest():

    def http_request(self, url=None, query_parameters=None, request_parameters=None, http_method=None, headers=None, cookies=None):
        try:
            if http_method.upper() == 'GET':
                res = requests.get(url=url, params=query_parameters, headers=headers, cookies=cookies, verify=False)

            elif http_method.upper() == 'POST':
                res = requests.post(url=url, params=query_parameters, json=request_parameters, headers=headers, cookies=cookies, verify=False)

            elif http_method.upper() == 'DELETE':
                res = requests.delete(url=url, params=request_parameters, headers=headers, cookies=cookies, verify=False)

            elif http_method.upper() == 'PUT':
                res = requests.put(url=url, json=request_parameters, headers=headers, cookies=cookies, verify=False)

            else:
                logger.error('输入的请求方法不正确')
        except Exception as e:
            logger.error("请求出错了{0}".format(e))
            raise e
        return res
