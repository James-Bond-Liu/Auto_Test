# !@coding  :utf-8
# !@Time    :2021/1/7 19:48
# !@Author  :liulei

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import process_bill, account_home


class Bill(BasePage):
    """
    账套-设置-账单中的功能
    """

    def import_bill(self):
        case_name = '导入账单'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.enter_page_too(account_home.ywcl, process_bill.bill, process_bill.change_iframe)
            self.import_flow()
            self.sleep(2)
            check_info = self.check_data(process_bill.check_page, account_set_setting_data.bill_import_check)

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def import_flow(self):
        self.select_text(*process_bill.select_account, account_set_setting_data.bill_select)
        self.click(*process_bill.ipt_bill)
        self.send_keys(*process_bill.upload, account_set_setting_data.bill_data)
        self.sleep(5)
        self.click(*process_bill.next_step)

    def check_bill_data(self):
        case_name = '检查账单数据并查看汇总'
        print(case_name, "|开始执行")

        check_info = None
        income_list = []
        expense_list = []

        try:

            self.click(*process_bill.income_filter)
            self.select_value(*process_bill.page_limit, value='500')
            self.sleep(5)
            for i in range(1, 275):
                info = self.get_element_text('xpath', process_bill.income_money % i)
                info = info.replace(',', '')
                income_list.append(float(info))
            print(income_list)
            income = ('%.2f' % sum(income_list))

            self.click(*process_bill.expense_filter)
            self.sleep(5)
            for i in range(1, 246):
                info = self.get_element_text('xpath', process_bill.expense_money % i)
                info = info.replace(',', '')
                expense_list.append(float(info))
            print(expense_list)
            expense = ('%.2f' % sum(expense_list))

            self.click(*process_bill.all_filter)
            self.sleep(2)
            self.click(*process_bill.view_amount)
            amount_income = (self.get_element_text(*process_bill.amount_income)).replace(',', '')
            amount_expense = (self.get_element_text(*process_bill.amount_expense)).replace(',', '')

            print('income:', income)
            print('expense:', expense)
            print('amount_income:', amount_income)
            print('amount_expense:', amount_expense)

            if income == amount_income and expense == amount_expense:
                check_info = True

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def clear_bill(self):
        case_name = '清空账单设置'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:

            self.select_value(*process_bill.page_limit, value='500')
            self.sleep(5)
            self.click(*process_bill.select_all)
            self.sleep(1)
            self.click(*process_bill.more_func)
            self.click(*process_bill.more_delete)
            self.click(*process_bill.delete_confirm)

            self.sleep(5)
            self.click(*process_bill.select_all)
            self.click(*process_bill.more_func)
            self.click(*process_bill.more_delete)
            self.click(*process_bill.delete_confirm)
            self.sleep(5)
            check_info = self.check_data(process_bill.check_page, account_set_setting_data.bill_clear_check)
            self.import_flow()

        except Exception as why:
            print('why', why)
        #
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def batch_register(self):
        case_name = '批量登记'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:

            self.click(*process_bill.income_filter)
            self.click(*process_bill.select_all)
            self.click(*process_bill.batch_register)
            self.click(*process_bill.ipt_transaction)
            self.click(*process_bill.select_transaction)
            self.click(*process_bill.register_btn)

            check_info = self.check_data(process_bill.check_register_status,
                                         account_set_setting_data.bill_register_check)

        except Exception as why:
            print('why', why)
        #
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def batch_vouch(self):
        case_name = '批量登记'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.click(*process_bill.income_filter)
            self.click(*process_bill.select_all)
            self.click(*process_bill.batch_vouch)
            self.click(*process_bill.vouch_confirm)

            check_info = self.check_data(process_bill.check_vouch_status, None, 2)

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def delete_register_vouch(self):
        case_name = '删除账单凭证并取消登记'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.click(*process_bill.income_filter)
            self.click(*process_bill.select_all)
            self.click(*process_bill.more_func)
            self.click(*process_bill.delete_vouch_confirm)
            self.click(*process_bill.vouch_confirm)
            self.sleep(2)

            self.click(*process_bill.select_all)
            self.click(*process_bill.more_func)
            self.click(*process_bill.delete_register)
            self.click(*process_bill.delete_register_confirm)

            vouch_info = self.check_data(process_bill.check_vouch_status, None)
            register_info = self.check_data(process_bill.check_register_status,
                                            account_set_setting_data.bill_delete_register_check)

            if vouch_info and register_info:
                check_info = True

        except Exception as why:
            print('why', why)
        #
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
