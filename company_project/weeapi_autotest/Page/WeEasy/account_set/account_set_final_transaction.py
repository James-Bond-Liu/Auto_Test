# !@coding  :utf-8 
# !@Time    :2021/4/3 13:34
# !@Author  :LiuLei
from Page.BasePage import BasePage
from element.WeEasy.el_account_set import finance_final_transaction, account_home
from data.config import account_set_setting_data


class FinalTransaction(BasePage):
    
    """期末结转"""
    
    @BasePage._base
    def finaltransaction(self):
        case_name = '上月期末结转'
        print(case_name, "|开始执行")
        check_info = False
        try:

            info = self.change_payment_days()
            self.enter_page_too(account_home.finance, finance_final_transaction.final_page, finance_final_transaction.change_iframe)
            self.click(*finance_final_transaction.jzbtn)
            self.sleep(1)
            self.click(*finance_final_transaction.jz_confirm)
            check_info = self.check_data(finance_final_transaction.fiscal_period, info)
        except Exception as why:
            print(why)
        return case_name, check_info
    
    def change_payment_days(self):
        """切换账期"""
        try:
            info = self.get_element_text(*finance_final_transaction.fiscal_period)
            month = info.split('年')[0]+'年0'+info.split('年')[1]
            print(month)
            self.move(*finance_final_transaction.fiscal_period)
            self.click('xpath', finance_final_transaction.payment_days % month)
            return info
        except Exception as why:
            print('why', why)
