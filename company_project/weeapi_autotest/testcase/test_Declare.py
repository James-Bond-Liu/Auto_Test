# !@coding  :utf-8 
# !@Time    :2021/2/20 17:41
# !@Author  :LiuLei
import pytest

from Page.WeEasyDeclareTest.jiangsu.declare import RoutineCheckDeclare


@pytest.mark.declare
# @pytest.mark.debug
# 登录
def test_declare_status_check(init_weeasy_programs):
    RoutineCheckDeclare(init_weeasy_programs).declare_status_check()
