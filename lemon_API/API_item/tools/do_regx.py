# -*- coding: utf-8 -*-
# @Time :2020/7/12 17:32
# @Author : liufei
# @File :do_regx.PY

import re
from API_item.tools.get_data import GetData

class DoRegx():
    def do_regx(s):
        while re.search('\$\{(.*?)\}',s):
            key=re.search('\$\{(.*?)\}',s).group() #${normal_tel}
            value=re.search('\$\{(.*?)\}',s).group(1) #normal_tel
            s = s.replace(key,str(getattr(GetData,value)))
        return s
if __name__ == '__main__':
    s = "{'sql':'select LeaveAmount from member where MobilePhone=${normal_tel}'}"
    print(DoRegx.do_regx(s))