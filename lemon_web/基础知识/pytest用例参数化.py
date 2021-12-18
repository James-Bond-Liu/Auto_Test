# -*- coding: utf-8 -*-
# @Time :2020/10/24 17:57
# @Author : liufei
# @File :pytest用例参数化.PY
import pytest

# 测试用例的参数化
'''
pytest.mark.parametrize(“参数名”,列表数据) --pytest中用例参数化
当测试用例需要多个数据时，我们可以使用嵌套序列(嵌套元组&嵌套列表)的列表来存放测试数据
装饰器@pytest.mark.parametrize()可以使用单个变量接收数据，也可以使用多个变量接收，同样，测试用例函数也需要与其保持一致
当使用单个变量接收时，测试数据传递到测试函数内部时为列表中的每一个元素或者小列表，需要使用索引的方式取得每个数据
当使用多个变量接收数据时，那么每个变量分别接收小列表或元组中的每个元素
列表嵌套多少个多组小列表或元组，测生成多少条测试用例
一个测试函数还可以同时被多个参数化装饰器装饰，那么多个装饰器中的数据会进行交叉组合的方式传递给测试函数，
进而生成n*n个测试用例，这也为我们的测试设计时提供了方便
'''

# 方法一
import pytest
@pytest.mark.parametrize("inputed,excepted", [("9+1", 10), ("9+2", 11), ("1+1", 2)])
def test_eval(inputed,excepted):
    assert (eval(inputed)==excepted)
#9+1=10，
#9+2=11,
#1+1=2
if __name__=="__main__":
    pytest.main(["-s","pytest用例参数化.py"])

#方法二
name_list = ['lisi', 'wanghui', 'zhouchuanlun']
@pytest.mark.parametrize('name', name_list)
def test_name(name):
    print(name)
#lisi,
#wanghui,
#zhouchuanlun
if __name__ == "__main__":
    pytest.main(["-s", "pytest用例参数化.py"])

#方法三
#多个参数化参数的所有组合
@pytest.mark.parametrize("x",["a","b"])
@pytest.mark.parametrize("y",[2,3])
def test_foo(x,y):
    print("测试数据组合:x->%s,y->%s"%(x,y))
#a,2
#a,3
#b,2
#b,3
if __name__=="__main__":
    pytest.main(["-s","pytest用例参数化.py"])
