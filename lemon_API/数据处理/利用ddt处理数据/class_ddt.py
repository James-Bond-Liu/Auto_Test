# -*- coding: utf-8 -*-
# @Time :2020/6/20 19:58
# @Author : liufei
# @File :class_ddt.PY

#测试用例是不能传参数的，但是在利用ddt装饰类和data装饰用例（方法）之后，便可以在函数中传入参数
import unittest
from ddt import ddt,data,unpack

@ddt
class Math(unittest.TestCase):

# 对纯列表数据进行unpack
    test_data1=[[1,3],[2,4],[6,7]]
    @data(*test_data1)  #  *test_data1 加上*号后，对数据test_data1脱掉外套，变成三组数据
                        #  当然也可以不带*直接传入test_data1
                        #  通过test_data1拿到几个数据，就执行几次用例，例如上面的数据拿到3个数据

    @unpack             #利用unpack进行数据拆解(每一条数据按照“,逗号”)时，尽量保证每条数据的个数保证一致
    def test_print_data(self,a,b):
        print(a)
        print(b)
    # test_data2=[{'number':'1234','name':'李二牛'},{'number':75678,'name':'何晨光'}]
#列表中嵌套字典
    # 传入字典类型数据
    # @data(*test_data2)
    # def test_print_data(self,a):
    #     print(a)

    #对字典类型数据进行unpack
    # @data(*test_data2)
    # @unpack
    # def test_print_data(self,number,name):
    #     print(number)
    #     print(name)