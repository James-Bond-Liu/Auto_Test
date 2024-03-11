# -*- coding: utf-8 -*-
# @Time :2020/7/14 21:14
# @Author : liufei
# @File :get_variable.PY

import pandas as pd

class GetVariable():
    init = pd.read_excel(r'../test_data/test_data.xlsx', sheet_name='init')
    cookie = None
    loanId = None
    NoRegTel = init.iloc[0, 0]
    NoRegTelR = 123456789
    normal_tel = init.iloc[1, 0]
    admin_tel = init.iloc[2, 0]
    loan_member_id = init.iloc[3, 0]
    member_id = init.iloc[4, 0]