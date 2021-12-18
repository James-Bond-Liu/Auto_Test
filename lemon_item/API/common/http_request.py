# -*- coding: utf-8 -*-
# @Time :2020/7/13 19:37
# @Author : liufei
# @File :http_request.PY

import requests
from API.common.do_logging import Dologging

class HttpRequest():

    def http_request(self, url, data, http_method, cookie=None):
        global res
        logger = Dologging().do_logging()
        try:
            if http_method.lower() == 'get':
                res = requests.get(url=url, params=data, cookies=cookie)
            elif http_method.lower() == 'post':
                res = requests.post(url=url, data=data, cookies=cookie)
            else:
                logger.error('请求方法有误')
        except Exception as e:
            logger.error('请求出错{0}'.format(e))
            raise e
        return res