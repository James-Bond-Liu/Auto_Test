
# -*- coding: utf-8 -*-
# @Time :2021/8/3 19:26
# @Author : liufei
# @File :处理多个excel+sheet.PY

"""
在接口自动化框架中处理多个excel文件，每个excel有多个sheet表单

先获取所有的Excel文件名

循环遍历所有文件名

    获取文件中的所有表单名

    对表单名进行循环遍历

        调用接口，对每个表单的所有用例执行操作

"""

"""利用pandas获取所有表单sheet的数据"""
import pandas as pd

# 获取文件中所有的表单名sheet_names.sheet_names
sheet_names = pd.ExcelFile(r'../基础知识\test_data.xlsx')
test_data = []
# 获取excel文件中所有sheet表单中的所有数据
for sheet in sheet_names.sheet_names:
    data = pd.read_excel(r'../web\test_data.xlsx', sheet_name=sheet, header=0)
    rows = data.index.values
    for i in rows:
        row_data = data.loc[i, ['case_id', 'url', 'data', 'title', 'http_method', 'expected', 'result', 'test_result']].to_dict()
        test_data.append(row_data)
print(test_data)
