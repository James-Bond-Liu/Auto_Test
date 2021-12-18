# coding: utf-8

import os
import subprocess
import sys
import datetime

try:
    run_type = sys.argv[1]
    now = ((((str(datetime.datetime.now()))[4:16]).replace(' ', '')).replace('-', '')).replace(':', '')
    if run_type == 'all':
        shell_all = r"pytest %s -s --capture=no" % (os.getcwd())
        subprocess.Popen(shell_all, shell=True)
    elif run_type == 'debug' or run_type == 'declare':
        shell_all = r"pytest %s -s --capture=no -m=%s --html=./debug_log/%s.html" % (os.getcwd(), run_type, now)
        subprocess.Popen(shell_all, shell=True)
    else:
        shell_all = r"pytest %s -s --capture=sys -m=%s --html=./report/report_%s.html" % (os.getcwd(), run_type, now)
        print(shell_all)
        subprocess.Popen(shell_all, shell=True)

except IndexError as why:
    print('请输入正确的运行方式！')
    exit()
