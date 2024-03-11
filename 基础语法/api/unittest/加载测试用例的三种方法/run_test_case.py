# -*- coding: utf-8 -*-
# @Time :2020/6/13 17:54
# @Author : liufei
# @File :class_unittest02.PY

                                                # 在其他模块中执行测试用例

import unittest
from 基础语法.api.unittest.加载测试用例的三种方法.test_case import TestMathMethod1

# 方法一，逐条加载测试用例，每一条测试用例就是用例所在类的一个实例，并且需要在测试类后面传入测试方法名（用例名）参数
# 利用此方法在非测试用例所在模块执行测试用例时，一个实例就是一条测试用例，详情如下：
suite1=unittest.TestSuite() #利用TestSuite()类来创建一个容器
suite1.addTest(TestMathMethod1('test_add_two_postive')) #一条测试用例
suite1.addTest(TestMathMethod1('test_add_two_negative')) #一条测试用例
runner1=unittest.TextTestRunner()
runner1.run(suite1)

# 方法二,根据测试类来加载测试用例，调用加载器下的loadTestsFromTestCase()方法，将某个类下的所有测试用例全部加载到容器中
# #loadTestsFromTestCase()方法需要传入参数——测试用例所在类的类名

suite2=unittest.TestSuite()
loader2=unittest.TestLoader() #利用TestLoader()类来创建一个加载器
suite2.addTest(loader2.loadTestsFromTestCase(TestMathMethod1))
runner2=unittest.TextTestRunner()
runner2.run(suite2)

# 方法三，将某个模块（文件）下的所有测试用例，利用加载器下的loadTestsFromModule()方法将所有的测试用例加载到容器中
# #loadTestsFromModule()需要传入参数——模块名,注意在传入该模块之前需要先导入模块
"""常用此方法直接加载模块下所有的测试用例"""
suite3=unittest.TestSuite()
loader3=unittest.TestLoader()
from 基础语法.api.unittest.加载测试用例的三种方法 import test_case
suite3.addTest(loader3.loadTestsFromModule(test_case))
import HTMLTestRunnerNew #第三方输出测试报告的工具
with open(r'./test_report.html','wb') as file:
    runner3=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description='第一次单元测试报告')
    runner3.run(suite3)

#方法四：利用discover方法收集测试用例
case_path = r''  #代表当前目录
discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
'''
1.discover方法里面有三个参数：
start_dir:这个是待执行用例的目录。
pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。
top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。
2.discover加载到的用例是一个list集合，需要重新写入到一个list对象testcase里，这样就可以用unittest里面的TextTestRunner这里类的run方法去执行。
'''
runner4 = unittest.TextTestRunner()
runner4.run(discover)

#方法五：利用addTests方法加载测试用例
from 基础语法.api.unittest.加载测试用例的三种方法.test_case import TestMathMethod1
from 基础语法.api.unittest.加载测试用例的三种方法.test_case import TestMathMethod2
suite = unittest.TestSuite()
#将用例添加在一起形成一个列表集合
case_list = [TestMathMethod1('test_add_two_postive'), TestMathMethod1('test_add_two_zero'),
             TestMathMethod2('test_multi_two_postive'), TestMathMethod2('test_multi_two_zero')]
#addTests方法加载测试用例集合
suite.addTests(case_list)
runner5 = unittest.TextTestRunner()
runner5.run(suite)

# 文件读写操作
# r 只能读
# r+可读可写，不会创建不存在的文件。如果直接写文件，则从顶部开始写，覆盖之前此位置的内容（并不是原文件内容全部消失，仅代表原位置的内容被覆盖掉，其余文件内容依然存在不受影响），如果先读后写，则会在文件最后追加内容。
# w+ 可读可写 如果文件存在 则覆盖整个文件（原文件中的所有内容均被覆盖），不存在则创建，必须先写后读，且要移动文件指针
# w 只能写 覆盖整个文件 不存在则创建
# a 只能写 从文件底部添加内容 不存在则创建
# a+ 可读可写  永远从文件底部添加内容 不存在则创建，文件指针在最后，读需要移动文件指针

