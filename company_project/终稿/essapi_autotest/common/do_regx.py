# -*- coding: utf-8 -*-

import re
from conf.global_data import GlobalData


class DoRegx():
    def do_regx(self, s):
        while re.search("\$\{(.*?)\}", s):
            key = re.search("\$\{(.*?)\}", s).group(0)
            value = re.search("\$\{(.*?)\}", s).group(1)
            s = s.replace(key, str(getattr(GlobalData, value)))
        return s
