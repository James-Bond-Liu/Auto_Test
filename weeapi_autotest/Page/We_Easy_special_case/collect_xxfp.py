# !@coding  :utf-8 
# !@Time    :2021/1/9 14:59
# !@Author  :liulei

from Page.BasePage import BasePage
from element.WeEasy.el_account_set import process_expense_invoice, account_home


class Xxfp(BasePage):
    """
    账套-设置-进项发票中的功能
    """

    def collect_xxfp(self):
        case_name = '采集消项发票'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.enter_page_too(account_home.ywcl, process_expense_invoice.xxfp, process_expense_invoice.change_iframe)
            self.click(*process_expense_invoice.more_func)
            self.click(*process_expense_invoice.collect)
            self.sleep(2)
            self.click(*process_expense_invoice.collect_confirm)
            self.sleep(2)
            self.click(*process_expense_invoice.collect_confirm)
            self.sleep(60)
            check_info = self.check_collect()

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def check_collect(self):
        n = 10
        info = None
        check_info = None
        while n > 0:
            self.sleep(10)
            try:
                self.click(*process_expense_invoice.refresh_btn)
                info = self.get_element_text(*process_expense_invoice.check_xxfp_collect)
            except Exception as why:
                print(why)
            print(info[3:6])
            if int(info[3:6]) != 0:
                check_info = True
                break

        return check_info

    def create_voucher(self):
        case_name = '生成凭证'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:

            self.enter_page_too(account_home.ywcl, process_expense_invoice.xxfp, process_expense_invoice.change_iframe)
            input("正在等待您手动填写好所有发票\n如果您填写完毕请按回车键：")
            self.click(*process_expense_invoice.select_all)
            self.click(*process_expense_invoice.create_vouch)
            self.click(*process_expense_invoice.create_vouch_confirm)

            check_info = self.check_data(process_expense_invoice.check_vouch_num, None, 2)

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
