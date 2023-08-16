# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ess_api
# @File     :do_regx
# @Date     :2021/10/22 10:41
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import re
from company_project.essapi_autotest_unitest.conf.global_data import GlobalData

class DoRegx():
    def do_regx(self, s):
        while re.search("\$\{(.*?)\}", s):
            key = re.search("\$\{(.*?)\}", s).group(0)
            value = re.search("\$\{(.*?)\}", s).group(1)
            s = s.replace(key, str(getattr(GlobalData, value)))
        return s