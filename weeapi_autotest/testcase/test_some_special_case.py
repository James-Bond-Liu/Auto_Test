# !@coding  :utf-8
# !@Time    :2021/1/9 11:41
# !@Author  :liulei
import pytest

from Page.We_Easy_special_case.collect_jxfp import Jxfp
from Page.We_Easy_special_case.collect_xxfp import Xxfp
from Page.We_Easy_special_case.swbb import Swbb
from Page.We_Easy_special_case.swbb_guangdong_zzs_comparison import SwbbComparison
from Page.We_Easy_special_case.import_invoice import Login


# @pytest.mark.special
# @pytest.mark.debug
# 采集进项发票
def test_collect_jxfp(init_weeasy_programs):
    Jxfp(init_weeasy_programs).collect_jxfp()


# @pytest.mark.special
# @pytest.mark.debug
# 进项发票生产凭证
def test_jxfp_create_voucher(init_weeasy_programs):
    Jxfp(init_weeasy_programs).create_voucher()


# @pytest.mark.special
# @pytest.mark.debug
# 采集销项发票
def test_collect_xxfp(init_weeasy_programs):
    Xxfp(init_weeasy_programs).collect_xxfp()


# @pytest.mark.special
# @pytest.mark.debug
# 销项发票生成凭证
def test_xxfp_create_voucher(init_weeasy_programs):
    Xxfp(init_weeasy_programs).create_voucher()


# @pytest.mark.special
# @pytest.mark.debug
# 税务报表取数
def test_swbb_qushu(init_weeasy_programs):
    Swbb(init_weeasy_programs).qushu()


# @pytest.mark.special
# @pytest.mark.debug
# 申报税款
def test_swbb_shenbao(init_weeasy_programs):
    Swbb(init_weeasy_programs).shenbao()


# @pytest.mark.special
# @pytest.mark.debug
# 申报税款
def test_swbb_SwbbComparison(init_weeasy_programs):
    SwbbComparison(init_weeasy_programs).zzs_comparison()


@pytest.mark.special
# @pytest.mark.debug
# 申报税款
def test_login_add_business(init_weeasy_programs):

    Login(init_weeasy_programs).add_costomer()


@pytest.mark.special
# @pytest.mark.debug
def test_im(init_weeasy_programs):
    Login(init_weeasy_programs).login()
    Login(init_weeasy_programs).import_invoice()
