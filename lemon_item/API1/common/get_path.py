# -*- coding: utf-8 -*-
# @Time :2020/7/16 22:12
# @Author : liufei
# @File :get_path.PY

import os

project_path=os.path.split(os.path.realpath(os.getcwd()))[0]

test_data_path=os.path.join(project_path, 'test_data', 'test_data.xlsx')

case_config_path=os.path.join(project_path, 'conf', 'case.config')

test_result_html_path=os.path.join(project_path, 'test_result', 'html', 'test_result.html')

test_log_path=os.path.join(project_path, 'test_log','test_log.txt')
print(test_data_path)

