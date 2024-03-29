# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ESS_API
# @File     :path
# @Date     :2021/8/16 15:31
# @Author   :LiuFei
# @Email    :fei.liu@hxgroup.com
# @Software :PyCharm
-------------------------------------------------
"""
import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
excel_data = os.path.join(project_path, 'data')
log_path = os.path.join(project_path, 'log', 'running_log.txt')
html_report_path = os.path.join(project_path, 'report', 'test_report.html')
txt_report_path = os.path.join(project_path, 'report', 'test_report.txt')
conf_path = os.path.join(project_path, 'conf', 'conf.ini')