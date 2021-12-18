# !@coding  :utf-8 
# !@Time    :2021/1/18 11:08
# !@Author  :liulei

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_invoice_rule, account_home


class Rule(BasePage):
    """
    账套-设置-账单中的功能
    """

    def create_rule(self):
        case_name = '创建发票规则'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.page_refresh()
            self.move(*account_home.setting)
            # self.sleep(1)
            self.click(*set_invoice_rule.invoice_rule)
            self.switch_to_frame(*set_invoice_rule.change_iframe)

            self.click(*set_invoice_rule.create_new_rule)
            for i in account_set_setting_data.invoice_rule:
                if i == account_set_setting_data.invoice_rule[2]:
                    self.create_rule_flow(i, invoice_type=1)
                else:
                    self.create_rule_flow(i)
            check_info = self.check_data(set_invoice_rule.create_tips, '匹配规则创建成功')
        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def create_rule_flow(self, costomer, invoice_type=None):

        if invoice_type:
            self.select_value(*set_invoice_rule.invoice_type, value='income')
            self.click(*set_invoice_rule.ipt_item)
            self.click(*set_invoice_rule.select_item_type)
            self.click(*set_invoice_rule.item_showall)
            self.click(*set_invoice_rule.select_item)
            self.click(*set_invoice_rule.click_i)
        self.click(*set_invoice_rule.costomer_box)
        self.send_keys(*set_invoice_rule.ipt_costomer, costomer)
        print('xxx')
        self.click(*set_invoice_rule.ipt_transaction)
        if invoice_type:
            self.click(*set_invoice_rule.select_expense_transaction)
        else:
            self.click(*set_invoice_rule.select_income_transaction)
        self.click(*set_invoice_rule.create_btn)
