# !@coding  :utf-8
# !@Time    :2021/1/5 20:42
# !@Author  :LiuLei

import pytest
from Page.WeEasy.account_set.account_set_assets_class import AssetsClass
from Page.WeEasy.account_set.account_set_bank import AccountSet
from Page.WeEasy.account_set.account_set_bill import Bill
from Page.WeEasy.account_set.account_set_com_go import OtherComGo
from Page.WeEasy.account_set.account_set_costomer import Costomer
from Page.WeEasy.account_set.account_set_expense_invoice import Xxfp
from Page.WeEasy.account_set.account_set_history import History
from Page.WeEasy.account_set.account_set_income_invoice import Jxfp
from Page.WeEasy.account_set.account_set_invoice_rule import Rule
from Page.WeEasy.account_set.account_set_payroll import PayRoll
from Page.WeEasy.account_set.account_set_people_register import PeopleRegister
from Page.WeEasy.account_set.account_set_product import Product
from Page.WeEasy.account_set.account_set_qcye_set import QcyeSet
from Page.WeEasy.account_set.account_set_receipts_register import ReceiptsRegister
from Page.WeEasy.account_set.account_set_sections import Sections
from Page.WeEasy.account_set.account_set_subject import Subject
from Page.WeEasy.account_set.account_set_supplier import Supplier
from Page.WeEasy.account_set.account_set_tags import Tags
from Page.WeEasy.account_set.account_set_additional_deducation import AdditionalDeducation
from Page.WeEasy.account_set.account_set_deprecition import Deprecition
from Page.WeEasy.account_set.account_set_inventory import Inventory
from Page.WeEasy.account_set.account_set_cost_account import CostAccount
from Page.WeEasy.account_set.account_set_final_transaction import FinalTransaction

from Page.WeEasy.init import DeInit
from Page.WeEasy.declare import Declare
from Page.WeEasy.declare2 import Declare2
from Page.WeEasy.data_stcs import DataStcs
from Page.WeEasy.batch_operation import BatchOperation
from Page.WeEasy.cszb import Cszb
from Page.WeEasy.charge_manager import ChargeManager
from Page.WeEasy.wyk import Wyk
from Page.WeEasy.setting import Setting
from Page.WeEasy.business import BusinessManager
from Page.WeEasy.login import Login


@pytest.mark.we
# @pytest.mark.debug
# 登录
def test_login(init_weeasy_programs):
    Login(init_weeasy_programs).login_ts()


@pytest.mark.we
# # @pytest.mark.debug
# 删除客户
def test_tear_down(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).tear_down()


@pytest.mark.we
# # @pytest.mark.debug
# 添加企业
def test_add_business(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).add_business()


@pytest.mark.we
# # @pytest.mark.debug
# 删除企业
def test_delete_business(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).delete_business()


@pytest.mark.we
# # @pytest.mark.debug
# 停用企业
def test_block_business(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).block_business()


@pytest.mark.we
# # @pytest.mark.debug
# 批量停用企业
def test_batch_block_business(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).batch_block_business()


@pytest.mark.we
# # @pytest.mark.debug
# 批量启用企业
def test_batch_unblock_business(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).batch_unblock_business()


@pytest.mark.we
# # @pytest.mark.debug
# 批量删除企业
def test_batch_delete_business(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).batch_delete_business()


@pytest.mark.we
# # @pytest.mark.debug
# 新增企业曾用名
def test_batch_add_last_name(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).add_last_name()


@pytest.mark.we
# # @pytest.mark.debug
# 配置企业环境
def test_change_business_open_time(init_weeasy_programs):
    BusinessManager(init_weeasy_programs).change_business_open_time()


@pytest.mark.we
# # # @pytest.mark.debug
# 初始化界面检查
def test_check_init(init_weeasy_programs):
    DeInit(init_weeasy_programs).deinit_check_page()


@pytest.mark.we
# # # @pytest.mark.debug
# 申报界面检查
def test_check_declare(init_weeasy_programs):
    Declare(init_weeasy_programs).declare_data_page_check()


@pytest.mark.we
# # # @pytest.mark.debug
# 申报2.0界面检查
def test_check_declare2(init_weeasy_programs):
    Declare2(init_weeasy_programs).Declare2_page_check()


@pytest.mark.we
# # # @pytest.mark.debug
# 数据统计界面检查
def test_check_data_stcs(init_weeasy_programs):
    DataStcs(init_weeasy_programs).data_stcs_page_check()


@pytest.mark.we
# # # @pytest.mark.debug
# 批量操作界面检查
def test_check_batch_operation(init_weeasy_programs):
    BatchOperation(init_weeasy_programs).operation_page_check()


@pytest.mark.we
# # # @pytest.mark.debug
# 财税指标界面检查
def test_check_cszb(init_weeasy_programs):
    Cszb(init_weeasy_programs).cszb_page_check()


@pytest.mark.we
# # # @pytest.mark.debug
# 收费管理界面检查
def test_check_charge_manager(init_weeasy_programs):
    ChargeManager(init_weeasy_programs).charge_manager_page_check()


@pytest.mark.we
# # # @pytest.mark.debug
# 唯易客界面检查
def test_check_wyk(init_weeasy_programs):
    Wyk(init_weeasy_programs).wyk_check_page()


@pytest.mark.we
# # # @pytest.mark.debug
# 设置界面检查
def test_check_setting(init_weeasy_programs):
    Setting(init_weeasy_programs).settinh_page_check()


@pytest.mark.we
# # @pytest.mark.debug
# 增加银行账户
def test_add_account(init_weeasy_programs):
    AccountSet(init_weeasy_programs).add_account()


@pytest.mark.we
# # @pytest.mark.debug
# 删除银行账户
def test_delete_account(init_weeasy_programs):
    AccountSet(init_weeasy_programs).delete_account()


@pytest.mark.we
# # @pytest.mark.debug
# 增加客户
def test_add_costomer(init_weeasy_programs):
    Costomer(init_weeasy_programs).add_costomer()


@pytest.mark.we
# # @pytest.mark.debug
# 删除客户
def test_detele_costomer(init_weeasy_programs):
    Costomer(init_weeasy_programs).delete_costomer()


@pytest.mark.we
# # @pytest.mark.debug
# 增加供应商
def test_add_supplier(init_weeasy_programs):
    Supplier(init_weeasy_programs).add_supplier()


@pytest.mark.we
# # @pytest.mark.debug
# 删除供应商
def test_detele_supplier(init_weeasy_programs):
    Supplier(init_weeasy_programs).delete_supplier()


@pytest.mark.we
# # @pytest.mark.debug
# 增加其他往来
def test_add_com_go(init_weeasy_programs):
    OtherComGo(init_weeasy_programs).add_com_go()


@pytest.mark.we
# # @pytest.mark.debug
# 删除其他往来
def test_delete_com_go(init_weeasy_programs):
    OtherComGo(init_weeasy_programs).delete_com_go()


@pytest.mark.we
# # @pytest.mark.debug
# 增加项目
def test_add_product(init_weeasy_programs):
    Product(init_weeasy_programs).add_product()


@pytest.mark.we
# # @pytest.mark.debug
# 删除项目
def test_delete_product(init_weeasy_programs):
    Product(init_weeasy_programs).delete_product()


@pytest.mark.we
# # @pytest.mark.debug
# 新增部门
def test_add_sections(init_weeasy_programs):
    Sections(init_weeasy_programs).add_sections()


@pytest.mark.we
# # @pytest.mark.debug
# 删除部门
def test_delete_sections(init_weeasy_programs):
    Sections(init_weeasy_programs).delete_sections()


@pytest.mark.we
# # @pytest.mark.debug
# 新增标签
def test_add_tags(init_weeasy_programs):
    Tags(init_weeasy_programs).add_tags()


@pytest.mark.we
# # @pytest.mark.debug
# 删除标签
def test_delete_tags(init_weeasy_programs):
    Tags(init_weeasy_programs).delete_tags()


@pytest.mark.we
# # @pytest.mark.debug
# 新增资产类别
def test_add_assets_class(init_weeasy_programs):
    AssetsClass(init_weeasy_programs).add_assets_class()


@pytest.mark.we
# # @pytest.mark.debug
# 删除资产类别
def test_delete_assets_class(init_weeasy_programs):
    AssetsClass(init_weeasy_programs).delete_assets_class()


@pytest.mark.we
# # @pytest.mark.debug
# 新增二级科目
def test_add_subject(init_weeasy_programs):
    Subject(init_weeasy_programs).add_subject()


@pytest.mark.we
# # @pytest.mark.debug
# 删除二级科目
def test_delete_subject(init_weeasy_programs):
    Subject(init_weeasy_programs).delete_subject()


@pytest.mark.we
# # @pytest.mark.debug
# 创建发票规则
def test_create_rule(init_weeasy_programs):
    Rule(init_weeasy_programs).create_rule()


@pytest.mark.we
# # @pytest.mark.debug
# 导入期初余额
def test_import_qcye(init_weeasy_programs):
    QcyeSet(init_weeasy_programs).import_qcye()


@pytest.mark.we
# # @pytest.mark.debug
# 清空期初余额
def test_clear_qcye(init_weeasy_programs):
    QcyeSet(init_weeasy_programs).clear_qcye()


@pytest.mark.we
# # @pytest.mark.debug
# 导入历史凭据
def test_import_history(init_weeasy_programs):
    History(init_weeasy_programs).import_history()


@pytest.mark.we
# # @pytest.mark.debug
# 清空历史凭据
def test_delete_history(init_weeasy_programs):
    History(init_weeasy_programs).delete_history()


"""
折旧摊销
"""


@pytest.mark.we
# # @pytest.mark.debug
# 新增折旧摊销
def test_add_deprecition_item(init_weeasy_programs):
    Deprecition(init_weeasy_programs).add_deprecition_item()


@pytest.mark.we
# # @pytest.mark.debug
# 编辑折旧摊销
def test_edit_deprecition(init_weeasy_programs):
    Deprecition(init_weeasy_programs).edit_deprecition()


@pytest.mark.we
# # @pytest.mark.debug
# 删除折旧摊销
def test_delete_depercition(init_weeasy_programs):
    Deprecition(init_weeasy_programs).delete_depercition()


"""
存货设置
"""


@pytest.mark.we
# @pytest.mark.debug
# 新增存货类别
def test_add_inventory_type(init_weeasy_programs):
    Inventory(init_weeasy_programs).add_inventory_type()


@pytest.mark.we
# @pytest.mark.debug
# 新增存货
def test_add_inventory(init_weeasy_programs):
    Inventory(init_weeasy_programs).add_inventory()


@pytest.mark.we
# @pytest.mark.debug
# 删除存货
def test_delete_inventory(init_weeasy_programs):
    Inventory(init_weeasy_programs).delete_inventory()


""" 销项发票"""


@pytest.mark.we
# @pytest.mark.debug
# 导入销项发票
def test_import_xxfp(init_weeasy_programs):
    Xxfp(init_weeasy_programs).import_xxfp()


@pytest.mark.we
# @pytest.mark.debug
# 销项发票自动创建存货
def test_auto_create_inventory(init_weeasy_programs):
    Xxfp(init_weeasy_programs).auto_create_inventory()


@pytest.mark.we
# @pytest.mark.debug
# 检查发票信息
def test_xxfp_check_invoice_data(init_weeasy_programs):
    Xxfp(init_weeasy_programs).check_invoice_data()


@pytest.mark.we
# @pytest.mark.debug
# 销项发票查看汇总
def test_xxfp_check_invoice_amount(init_weeasy_programs):
    Xxfp(init_weeasy_programs).check_invoice_amount()


@pytest.mark.we
# @pytest.mark.debug
# 结算发票
def test_settlement_invoice(init_weeasy_programs):
    Xxfp(init_weeasy_programs).settlement_invoice()


@pytest.mark.we
# @pytest.mark.debug
# 销项批量发票结算
def test_xxfp_batch_settlement_invoice(init_weeasy_programs):
    Xxfp(init_weeasy_programs).batch_settlement_invoice()


@pytest.mark.we
# @pytest.mark.debug
# 删除结算
def test_xxfp_delete_settlement_invoice(init_weeasy_programs):
    Xxfp(init_weeasy_programs).delete_settlement_invoice()


@pytest.mark.we
# @pytest.mark.debug
# 销项发票-生成凭证
def test_xxfp_create_voucher(init_weeasy_programs):
    Xxfp(init_weeasy_programs).create_vouch()


@pytest.mark.we
# @pytest.mark.debug
# 销项发票-删除凭证
def test_xxfp_delete_voucher(init_weeasy_programs):
    Xxfp(init_weeasy_programs).delete_vouch()


@pytest.mark.we
# @pytest.mark.debug
# 销项发票-新增一个发票
def test_xxfp_add_invoice(init_weeasy_programs):
    Xxfp(init_weeasy_programs).add_invoice()


@pytest.mark.we
# @pytest.mark.debug
# 清空销项发票
def test_clear_xxfp(init_weeasy_programs):
    Xxfp(init_weeasy_programs).clear_xxfp()


@pytest.mark.we
# @pytest.mark.debug
# 销项项发票查询
def test_xxfp_invoice_filter(init_weeasy_programs):
    Xxfp(init_weeasy_programs).invoice_filter()


"""进项发票"""


@pytest.mark.we
# @pytest.mark.debug
# 导入进项发票
def test_import_jxfp(init_weeasy_programs):
    Jxfp(init_weeasy_programs).import_jxfp()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票检查数据
def test_jxfp_check_invoice_data(init_weeasy_programs):
    Jxfp(init_weeasy_programs).check_invoice_data()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票查看汇总
def test_jxfp_check_invoice_amount(init_weeasy_programs):
    Jxfp(init_weeasy_programs).check_invoice_amount()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票结算
def test_settlement_invoice(init_weeasy_programs):
    Jxfp(init_weeasy_programs).settlement_invoice()


@pytest.mark.we
# @pytest.mark.debug
# 进项批量发票结算
def test_batch_settlement_invoice(init_weeasy_programs):
    Jxfp(init_weeasy_programs).batch_settlement_invoice()


@pytest.mark.we
# @pytest.mark.debug
# 删除结算
def test_delete_settlement_invoice(init_weeasy_programs):
    Jxfp(init_weeasy_programs).delete_settlement_invoice()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票-生成凭证
def test_jxfp_create_voucher(init_weeasy_programs):
    Jxfp(init_weeasy_programs).create_voucher()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票,删除凭证
def test_jxfp_delete_vouch(init_weeasy_programs):
    Jxfp(init_weeasy_programs).delete_vouch()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票批量编辑
def test_jxfp_batch_edit(init_weeasy_programs):
    Jxfp(init_weeasy_programs).batch_edit()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票新增
def test_jxfp_add_invoice(init_weeasy_programs):
    Jxfp(init_weeasy_programs).add_invoice()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票自动补全
def test_jxfp_autocomple_invoice(init_weeasy_programs):
    Jxfp(init_weeasy_programs).autocomple()


@pytest.mark.we
# @pytest.mark.debug
# 删除进项发票
def test_delete_vouch(init_weeasy_programs):
    Jxfp(init_weeasy_programs).clear_jxfp()


@pytest.mark.we
# @pytest.mark.debug
# 进项发票查询
def test_invoice_filter(init_weeasy_programs):
    Jxfp(init_weeasy_programs).invoice_filter()


""" bom单"""


@pytest.mark.we
# @pytest.mark.debug
# 添加存货bom
def test_add_bom(init_weeasy_programs):
    Inventory(init_weeasy_programs).add_bom()


@pytest.mark.we
# @pytest.mark.debug
# 删除存货bom
def test_delete_bom(init_weeasy_programs):
    Inventory(init_weeasy_programs).delete_bom()


"""账单"""


@pytest.mark.we
# @pytest.mark.debug
# 导入账单
def test_import_bill(init_weeasy_programs):
    Bill(init_weeasy_programs).import_bill()


@pytest.mark.we
# @pytest.mark.debug
# 检查账单数据
def test_check_bill_data(init_weeasy_programs):
    Bill(init_weeasy_programs).check_bill_data()


@pytest.mark.we
# @pytest.mark.debug
# 检查账单数据
def test_clear_bill_data(init_weeasy_programs):
    Bill(init_weeasy_programs).clear_bill()


@pytest.mark.we
# @pytest.mark.debug
# 批量登记账单
def test_batch_register(init_weeasy_programs):
    Bill(init_weeasy_programs).batch_register()


@pytest.mark.we
# @pytest.mark.debug
# 账单批量生成凭证
def test_batch_vouch(init_weeasy_programs):
    Bill(init_weeasy_programs).batch_vouch()


@pytest.mark.we
# @pytest.mark.debug
# 账单删除凭证并取消登记
def test_delete_register_vouch(init_weeasy_programs):
    Bill(init_weeasy_programs).delete_register_vouch()


"""单据登记"""


@pytest.mark.we
# @pytest.mark.debug
# 单据登记
def test_add_receipts_register(init_weeasy_programs):
    ReceiptsRegister(init_weeasy_programs).add_receipts_register()


@pytest.mark.we
# @pytest.mark.debug
# 单据删除结算
def test_receipts_register_delete_statement(init_weeasy_programs):
    ReceiptsRegister(init_weeasy_programs).delete_statement()


@pytest.mark.we
# @pytest.mark.debug
# 单据结算
def test_receipts_register_statement(init_weeasy_programs):
    ReceiptsRegister(init_weeasy_programs).statement()


@pytest.mark.we
# @pytest.mark.debug
# 详细登记单据
def test_detail_register(init_weeasy_programs):
    ReceiptsRegister(init_weeasy_programs).detail_register()


@pytest.mark.we
# @pytest.mark.debug
# 删除单据
def test_receipts_register_delete_receipts(init_weeasy_programs):
    ReceiptsRegister(init_weeasy_programs).delete_receipts()


"""人员登记"""


@pytest.mark.we
# @pytest.mark.debug
# 新增境内人员登记
def test_people_register_add_cisborder_person(init_weeasy_programs):
    PeopleRegister(init_weeasy_programs).add_cisborder_person()


@pytest.mark.we
# @pytest.mark.debug
# 新增境外人员登记
def test_people_register_add_overseas_person(init_weeasy_programs):
    PeopleRegister(init_weeasy_programs).add_overseas_person()


@pytest.mark.we
# @pytest.mark.debug
# 批量编辑人员登记
def test_people_register_batch_edit(init_weeasy_programs):
    PeopleRegister(init_weeasy_programs).batch_edit()


@pytest.mark.we
# @pytest.mark.debug
# 删除人员登记
def test_people_register_delete_person(init_weeasy_programs):
    PeopleRegister(init_weeasy_programs).delete_person()


@pytest.mark.we
# @pytest.mark.debug
# 导入人员登记
def test_people_register_import_person(init_weeasy_programs):
    PeopleRegister(init_weeasy_programs).import_person()


"""薪酬表"""


@pytest.mark.we
# @pytest.mark.debug
# 添加薪酬表
def test_payroll_add_payroll(init_weeasy_programs):
    PayRoll(init_weeasy_programs).add_payroll()


@pytest.mark.we
# @pytest.mark.debug
# 薪酬表无数据时添加凭证
def test_payroll_null_data_create_vouch(init_weeasy_programs):
    PayRoll(init_weeasy_programs).payroll_no_price_create_vouch()


@pytest.mark.we
# @pytest.mark.debug
# 生产经营所得-核定征收编辑人员
def test_edit_payroll_first_type(init_weeasy_programs):
    PayRoll(init_weeasy_programs).edit_payroll_first_type()


@pytest.mark.we
# @pytest.mark.debug
# 正常工资薪金表编辑人员
def test_edit_payroll_second_type(init_weeasy_programs):
    PayRoll(init_weeasy_programs).edit_payroll_second_type()


@pytest.mark.we
# @pytest.mark.debug
# 外籍人员正常工资薪金编辑人员
def test_edit_payroll_third_type(init_weeasy_programs):
    PayRoll(init_weeasy_programs).edit_payroll_third_type()


@pytest.mark.we
# @pytest.mark.debug
# 全年一次性奖金收入编辑人员
def test_edit_payroll_fourth_type(init_weeasy_programs):
    PayRoll(init_weeasy_programs).edit_payroll_fourth_type()


@pytest.mark.we
# @pytest.mark.debug
# 劳务报酬(一般劳务、其他非连续劳务)
def test_edit_payroll_fifth_type(init_weeasy_programs):
    PayRoll(init_weeasy_programs).edit_payroll_fifth_type()


@pytest.mark.we
# @pytest.mark.debug
# 劳务报酬(保险营销员、证券经纪人、其他连续劳务)
def test_edit_payroll_sixth_type(init_weeasy_programs):
    PayRoll(init_weeasy_programs).edit_payroll_sixth_type()


@pytest.mark.we
# @pytest.mark.debug
# 薪酬表生成凭证
def test_payroll_create_vouch(init_weeasy_programs):
    PayRoll(init_weeasy_programs).payroll_create_vouch()


@pytest.mark.we
# @pytest.mark.debug
# 薪酬表设置
def test_edit_payroll_payroll_setting(init_weeasy_programs):
    PayRoll(init_weeasy_programs).payroll_setting()


"""
专项附加税扣除
"""


@pytest.mark.we
# @pytest.mark.debug
# 子女教育支出
def test_children_education_add_child(init_weeasy_programs):
    AdditionalDeducation(init_weeasy_programs).children_education_add_child()


@pytest.mark.we
# @pytest.mark.debug
# 继续教育支出
def test_continuew_deucation(init_weeasy_programs):
    AdditionalDeducation(init_weeasy_programs).continuew_deucation()


@pytest.mark.we
# @pytest.mark.debug
# 住房贷款利息支出
def test_housing_loans(init_weeasy_programs):
    AdditionalDeducation(init_weeasy_programs).housing_loans()


@pytest.mark.we
# @pytest.mark.debug
# 住房租金支出
def test_house_rents(init_weeasy_programs):
    AdditionalDeducation(init_weeasy_programs).house_rents()


@pytest.mark.we
# @pytest.mark.debug
# 赡养老人支出
def test_care_old(init_weeasy_programs):
    AdditionalDeducation(init_weeasy_programs).care_old()


@pytest.mark.we
# @pytest.mark.debug
# 上月期末结转
def test_proccess_finaltransaction(init_weeasy_programs):
    FinalTransaction(init_weeasy_programs).finaltransaction()


@pytest.mark.we
# @pytest.mark.debug
# 成本核算
def test_proccess_cost_account(init_weeasy_programs):
    CostAccount(init_weeasy_programs).proccess_cost_account()
