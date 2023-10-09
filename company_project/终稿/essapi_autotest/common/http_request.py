# -*- coding: utf-8 -*-

import requests
from common.out_log import OutLog

logger = OutLog().out_log()


class HttpRequest():

    def http_request(self, url, data, http_method, headers, cookies=None):
        try:
            if http_method.upper() == 'GET':
                res = requests.get(url=url, params=data, headers=headers, cookies=cookies, verify=False)

            elif http_method.upper() == 'POST':
                res = requests.post(url=url, json=data, headers=headers, cookies=cookies, verify=False)

            elif http_method.upper() == 'DELETE':
                res = requests.delete(url=url, params=data, headers=headers, cookies=cookies, verify=False)

            elif http_method.upper() == 'PUT':
                res = requests.put(url=url, json=data, headers=headers, cookies=cookies, verify=False)

            else:
                logger.error('输入的请求方法不正确')
        except Exception as e:
            logger.error("请求出错了{0}".format(e))
            raise e
        return res
