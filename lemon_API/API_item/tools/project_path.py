# -*- coding: utf-8 -*-
# @Time :2020/6/26 17:49
# @Author : liufei
# @File :project_path.PY

import os
'''专用来读取路径的位置'''
#os.path.realpath(__file__)获取当前文件所在的绝路路径，然后利用os.path.split将目录和文件拆分剥离，返回元组。
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试数据的路径
test_data_path=os.path.join(project_path,'test_data',"test_data.xlsx")

#测试报告的路径
test_report_path=os.path.join(project_path,'test_result','html_report','test_api.html')

#配置文件的路径
test_config_path=os.path.join(project_path,'conf','case.config')

#输出日志文件的路径
test_log_path=os.path.join(project_path,'test_result','log','test_api.txt')


