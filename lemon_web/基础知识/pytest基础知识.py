# -*- coding: utf-8 -*-
# @Time :2020/10/21 20:59
# @Author : liufei
# @File :pytest基础知识.PY

'''
    测试脚本，测试函数名都要以"test_"开头, 类名以"Test"开头
    测试类不需要继承unittest.TestCase, 测试类中不能有__init__方法
    默认从当前执行pytest命令的目录中开搜集测试用例
'''

# pytest中的断言，assert 表达式，判断这个表达式为True或False，通过或失败。
# 断言相等
assert 1+1 == 2
assert 1+2 != 2
assert 5 >= 4
assert {'a': 1, 'b': 2} == {'b':2, 'a':1}  # 也可用例判断列表和字典相等
# 断言包含
assert '百度' in driver.title
assert 1 in [1,2,3]
# 断言True/False/None
assert 3>2 is True
assert 3>2 is not False
assert [] is not None

'''
1.conftest.py文件名字是固定的，不可以做任何修改

2.文件和用例文件在同一个目录下，那么conftest.py作用于整个目录

3.conftest.py文件所在目录必须存在__init__.py文件

4.conftest.py文件不能被其他文件导入

5.所有同目录测试文件运行前都会执行conftest.py文件
'''

# 测试准备与环境清理 -Fixtures
'''
Pytest中的Test Fixtures方法有5种范围：
1.Session会话级：运行一次Pytest算一次会话。运行期间只setup/teardown一次
2.Package包级：对每个包Python包setup/teardown一次
3.Module模块级：对每个Python脚本setup/teardwon一次
4.Class级：对每个测试类setup/teardown一次
5.Function级/Method级：对每个测试函数、测试方法setup/teardown一次
'''

