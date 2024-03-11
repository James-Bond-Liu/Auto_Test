# -*- coding: utf-8 -*-
# @Time :2020/6/13 17:11
# @Author : liufei
# @File :class_unittest.PY

import unittest
from 基础语法.api.unittest.加载测试用例的三种方法.math_method import MathMethod

# 创建的测试用例类必须继承unittest下的TestCase类
class TestMathMethod1(unittest.TestCase):
    def setUp(self):
        print("开始执行测试用例")
    def test_add_two_postive(self):#测试用例的方法名必须以“test”开头，且测试用例不能传入参数。
        res=MathMethod(1,1).add()
        print('1+1的结果',res)
        try:
            self.assertEqual(2,res)
        except AssertionError as e:
            print('断言有问题')
            raise e

    def test_add_two_zero(self):
        res=MathMethod(0,0).add()
        print('0+0的结果',res)
        try:
            self.assertEqual(0, res, '断言失败')
        except AssertionError as e:
            print('断言有问题')
            raise e

    def tearDown(self):
        print("用例执行完成")

class TestMathMethod2(unittest.TestCase):
    def test_multi_two_postive(self):
        res=MathMethod(1,1).multi()
        print('1*1的结果',res)
    def test_multi_two_zero(self):
        res=MathMethod(0,0).multi()
        print('0*0的结果',res)

# 执行本模块中的所有测试用例
if __name__ == '__main__':
    unittest.main()  #默认情况下跑本模块下所有的测试用例