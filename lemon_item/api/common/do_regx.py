# -*- coding: utf-8 -*-
# @Time :2020/7/18 11:06
# @Author : liufei
# @File :do_regx.PY

import re
from lemon_item.api.common.get_variable import GetVariable

class DoRegx():
    def do_regx(s):
        while re.search('\$\{(.*?)\}',s):
            key=re.search('\$\{(.*?)\}',s).group()
            value=re.search('\$\{(.*?)\}',s).group(1)
            s = s.replace(key,str(getattr(GetVariable,value)))
        return s