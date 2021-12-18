# -*- coding: utf-8 -*-
# @Time :2020/8/10 19:51
# @Author : liufei
# @File :invest_data.PY

#投资成功
success = {'money': 1000}

#投资失败，投标置灰，非100的整数倍且大于100，非100的整数倍且小于100，字母，符号
no10 = [
{'money': 456, 'check': '请输入10的整数倍'},
{'money': 54, 'check': '请输入10的整数倍'},
{'money': 'a', 'check': '请输入10的整数倍'},
{'money': '$', 'check': '请输入10的整数倍'},
]

#投资失败，弹出框提示，负数负100整数倍金额，0，空格，100整数倍小于100，投标金额大于标剩余可投金额
wrong_format_money =  [
{'money': -10, 'check': '请正确填写投标金额'},
{'money': 0, 'check': '请正确填写投标金额'},
{'money': '', 'check': '请正确填写投标金额'},
{'money': 50, 'check': '请正确填写投标金额'},
]