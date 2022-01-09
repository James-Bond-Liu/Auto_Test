# -*- coding: utf-8 -*-
# @Time :2020/6/26 2:58
# @Author : liufei
# @File :get_cookie.PY

import pandas as pd
from lemon_API.API_item.tools.project_path import *
from lemon_API.API_item.tools.read_config import ReadConfig

class GetData():
    Cookie=None
    loanId=None
    check_list=eval(ReadConfig().get_config(test_config_path,'CHECKLEAVEAMOUNT','check_list'))
    NoRegTel = int(pd.read_excel(test_data_path,sheet_name='init').iloc[0,0])
    normal_tel = int(pd.read_excel(test_data_path, sheet_name='init').iloc[1, 0])
    admin_tel = int(pd.read_excel(test_data_path, sheet_name='init').iloc[2, 0])
    loan_member_id = int(pd.read_excel(test_data_path, sheet_name='init').iloc[3, 0])
    memberId = int(pd.read_excel(test_data_path, sheet_name='init').iloc[4, 0])

