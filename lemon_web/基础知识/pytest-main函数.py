# -*- coding: utf-8 -*-
# @Time :2020/8/16 21:23
# @Author : liufei
# @File :pytest-main函数.PY

import pytest
# pytest.main(args,plugins)
# args 传一个list对象，list 里面是多个命令行的参数
# plugins 传一个list对象，list 里面是初始化的时候需注册的插件
pytest.main(["命令参数1","命令参数2","命令参数3","...", "file_or_dir", "file_or_dir"])
#命令参数和测试用例都是可选的,file_or_dir==待执行的测试用例名/类名/模块名

pytest.main(["--html=report.html"])   #生成html测试报告,保存路径为相对路径下当前目录下命名为report.html
pytest.main(["--collect-only"])   #展示所有测试用例
pytest.main(["-k", "11"])      #使用指定表达式运行希望运行的用例
pytest.main(["-v", "-k", "11"])     # 增加-v查看详细信息
pytest.main(["-v", "-x"])   #-x 遇到错误即停止
pytest.main(["-v", "--maxfail=2", "--tb=no"])   #--maxfail=n 设定最多失败 n 次即停止
pytest.main(["-s"])     #允许终端运行时输出某些结果，例如print
pytest.main(["--lf"])   #定位失败的用例
pytest.main(["--ff"])   #定位失败的用例首先执行，但是正常的用例也会执行
pytest.main(["-q"])     #简化输出信息
pytest.main(["-l"])     #打印失败用例的变量值
pytest.main(["--duration=1"])   #只关心哪些部分是最慢的
pytest.main(["-h"])     #pytest的帮助选项

pytest.main(["-v", "-m=run_first"])  # 执行标签为‘run_first’的测试用例
"""
    使用-m对用例进行标记，用例需注释@pytest.mark.xxx,将xxx作为参数传入
    使用-m "mark1 and mark2"可以同时选中带有这两个标记的所有测试用例。
    使用-m "mark1 and not mark2"选中带哟与mark1的测试用例，而过滤掉带有mark2的测试用例
    使用-m "mark1 or mark2"则选中带有mark1或者mark2的所有测试用例
"""
pytest.main(["--tb=short"])
"""
    --tb=style,选择失败回溯信息
    short：仅输出assert一行以及系统判定内容(不显示上下文)
    no：不展示回溯信息
    line：只是用一行输出显示所有的信息错误，展示异常代码位置
    auto：只展示第一个和最后一个错误
    long：展示全部信息
    native：只展示puthon标准库信息，不展示额外信息
"""

#pytest指定测试范围
# 指定运行单个测试目录
pytest.main(['./test_case'])

# 指定运行单个测试文件
pytest.main(['./test_case/test_func.py'])

# 指定运行测试类
pytest.main(['./test_case/test_func.py::TestFunc'])


# 指定运行测试类中的某个方法
pytest.main(['./test_case/test_func.py::TestFunc::test_add_by_class'])

# 指定运行单个测试函数
pytest.main(['./test_case/test_func.py::test_add_by_func_aaa'])
