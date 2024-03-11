# -*- coding: utf-8 -*-
# @Time :2020/8/14 20:07
# @Author : liufei
# @File :path.PY

import os

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdata_dir = os.path.join(base_dir, 'TestDatas')

testcase_dir = os.path.join(base_dir, 'TestCases')

log_dir = os.path.join(base_dir, r'OutPuts\Logs')

screenshoot_dir = os.path.join(base_dir, 'OutPuts', 'ScreenShots')

report_dir = os.path.join(base_dir, 'OutPuts', 'Reports')
print(log_dir)