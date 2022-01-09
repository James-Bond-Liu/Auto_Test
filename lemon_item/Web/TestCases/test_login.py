# -*- coding: utf-8 -*-
# @Time :2020/8/6 21:00
# @Author : liufei
# @File :test_login.PY


from lemon_item.Web.PageObjects.index_page import IndexPage
from lemon_item.Web.TestDatas import login_data as LD
import pytest  #pytest和unittest不要放在一起用

'''测试用例=测试对象（功能）+测试数据'''

@pytest.mark.usefixtures('access_web')  #在运行测试用例的时候会先去运行access_web函数
@pytest.mark.usefixtures('refresh_page')    #同理，类下面的每个函数都会执行这个fixtures
class TestLogin():

    #在测试用例函数前打一个标签标记，此标签为冒烟标签。以便于利用pytest筛选用例然后执行。同一类型的标签，名称要一致。
    #利用pytest运行带有标签的测试用例，在终端Terminal上输入：pytest -m smoke（标签名）
    #正常用例，正常登录成功
    @pytest.mark.smoke
    # 传入需要接收返回值的fixture的函数名用来接收返回值。用fixture函数名称作为参数接收conftest.py文件中的函数的返回值。
    def test_1_login_success(self, access_web):
        # 步骤：输入用户名密码点击登录
        access_web[1].login(LD.success_data['user'], LD.success_data['password'])
        # 断言：页面中能否找到**元素,pytest中直接利用assert进行判断，后面表达式为Ture则返回Ture,False返回False
        assert IndexPage(access_web[0]).isExist_logout_element()

    #异常用例-手机号格式不正确(大于11位，小于11位，不在号码段，为空）
    @pytest.mark.parametrize('data1', LD.phone_data)    #pytest模块中不能使用ddt进行测试用例的参数化
    def test_0_login_user_wrongformat(self, data1, access_web):
        # 步骤：输入用户名密码点击登录
        access_web[1].login(data1['user'], data1['password'])
        # 断言：页面中提示请输入正确的手机号
        assert access_web[1].get_errorMsg_from_loginArea() == data1['check']

    #异常用例-手机号时未注册的,不输入密码,错误密码
    @pytest.mark.parametrize('data2', LD.password_data)
    def test_login_wrongPwd_noReg(self, data2, access_web):
        access_web[1].login(data2['user'], data2['password'])
        assert access_web[1].get_errorMsg_from_pageCenter() == data2['check']

