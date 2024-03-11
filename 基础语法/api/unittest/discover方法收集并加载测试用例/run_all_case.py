# -*- coding: utf-8 -*-
# @Time :2020/8/16 12:06
# @Author : liufei
# @File :run_all_case.PY

import unittest
#方法一
'''直接利用discover方法'''
case_path = r'/'  #代表当前目录的下一级
discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
runner = unittest.TextTestRunner()
runner.run(discover)

#方法二
'''在加载器loader中利用discover方法，更加简单'''
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.discover(case_path))
runner2=unittest.TextTestRunner()
runner2.run(suite)
'''
1.discover方法里面有三个参数：

start_dir:这个是待执行用例的目录。

pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。

top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。

2.discover加载到的用例是一个list集合，需要重新写入到一个list对象testcase里，这样就可以用unittest里面的TextTestRunner这里类的run方法去执行。
'''
