# !@coding  :utf-8 
# !@Time    :2021/1/15 14:42
# !@Author  :liulei
from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import process_receipts_register, account_home


class ReceiptsRegister(BasePage):
    """
    账套-设置-单据登记中的功能
    """

    def add_receipts_register(self):
        case_name = '新增单据'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            # self.login()
            self.enter_page_too(account_home.ywcl, process_receipts_register.receipts_register,
                                process_receipts_register.change_iframe)

            self.click(*process_receipts_register.unsettled)
            self.add_receipts(select=process_receipts_register.select_expense_transaction)

            self.click(*process_receipts_register.income_filter)
            self.click(*process_receipts_register.settled)
            self.add_receipts(select=process_receipts_register.select_income_transaction)

            check_info = self.check_data(process_receipts_register.register_check,
                                         account_set_setting_data.receipts_register_check)

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def add_receipts(self, select):
        self.send_keys(*process_receipts_register.date, '2020-12-31')
        self.click(*process_receipts_register.ipt_transaction)
        self.click(*select)
        self.send_keys(*process_receipts_register.ipt_money, account_set_setting_data.receipts_register_money)
        self.click(*process_receipts_register.ipt_costomer)
        self.click(*process_receipts_register.select_costomer)
        self.click(*process_receipts_register.register_btn)

    def statement(self):
        case_name = '结算单据'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.click(*process_receipts_register.page_refresh)
            self.click(*process_receipts_register.select_all)
            self.click(*process_receipts_register.batch_set_btn)
            self.click(*process_receipts_register.ipt_set_date)
            self.send_keys(*process_receipts_register.ipt_set_date, '2021-1-15')
            self.click(*process_receipts_register.set_btn)

            self.click(*process_receipts_register.set_confirm)
            check_info = self.check_data(process_receipts_register.tips,
                                         account_set_setting_data.receipts_register_set_tips)

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def delete_statement(self):
        case_name = '结算删除'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.click(*process_receipts_register.page_refresh)
            self.click(*process_receipts_register.select_all)
            self.click(*process_receipts_register.batch_set_btn)
            self.click(*process_receipts_register.delete_set)
            self.click(*process_receipts_register.delete_set_confirm)
            check_info = self.check_data(process_receipts_register.tips,
                                         account_set_setting_data.receipts_register_delete_tips)

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def detail_register(self):
        case_name = '详细登记单据'
        print(case_name, "|开始执行")

        check_info = None

        try:
            # self.login()
            # self.enter_page()
            self.click(*process_receipts_register.page_refresh)

            print('收入、结清')
            self.detail_reqister_flow(process_receipts_register.detail_income, process_receipts_register.detail_settled)
            # print('收入、未结算')
            # self.detail_reqister_flow(process_receipts_register.detail_income,
            #                           process_receipts_register.detail_unsettled)
            print('支出、结清')
            self.detail_reqister_flow(process_receipts_register.detail_expense,
                                      process_receipts_register.detail_settled)
            print('支出、未结算')
            self.detail_reqister_flow(process_receipts_register.detail_expense,
                                      process_receipts_register.detail_unsettled)

            self.click(*process_receipts_register.page_refresh)
            check_info = self.check_data(process_receipts_register.check_page,
                                         account_set_setting_data.receipts_register_detail_add_check)

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def delete_receipts(self):
        case_name = '删除单据'
        print(case_name, "|开始执行")

        check_info = None

        try:
            self.click(*process_receipts_register.page_refresh)
            self.click(*process_receipts_register.select_all)
            self.click(*process_receipts_register.delete_receipts)
            self.click(*process_receipts_register.delete_receipts_confirm)

            check_info = self.check_data(process_receipts_register.check_page,
                                         account_set_setting_data.receipts_register_delete_check)

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def detail_reqister_flow(self, io, set_status):
        self.click(*process_receipts_register.ipt_edit_detail)
        self.sleep(1)
        self.click(*io)
        self.click(*set_status)
        self.click(*process_receipts_register.detail_costomer)
        self.click(*process_receipts_register.detail_select_costomer_type)
        self.sleep(0.5)
        self.click(*process_receipts_register.detail_select_costomer)
        self.click(*process_receipts_register.detail_transaction)
        self.sleep(0.5)
        self.click(*process_receipts_register.detail_select_transaction)
        self.click(*process_receipts_register.detail_save_btn)
        self.clear(*process_receipts_register.detail_amount)
        self.send_keys(*process_receipts_register.detail_amount, '10000')
        self.sleep(0.5)
        self.click(*process_receipts_register.detail_save_btn)
        self.sleep(2)
