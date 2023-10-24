# -*- coding: utf-8 -*-
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import re
from conf.global_data import GlobalData


class DoRegx():
    def do_regx(self, s):
        while re.search("\$\{(.*?)\}", s):
            key = re.search("\$\{(.*?)\}", s).group(0)
            value = re.search("\$\{(.*?)\}", s).group(1)
            s = s.replace(key, str(getattr(GlobalData, value)))
        return s
