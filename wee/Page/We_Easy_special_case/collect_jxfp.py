# !@coding  :utf-8 
# !@Time    :2021/1/9 14:59
# !@Author  :liulei

from Page.BasePage import BasePage
from element.WeEasy import el_business_manager
from element.WeEasy import el_home_page
from element.WeEasy.el_account_set import process_income_invoice, account_home


class Jxfp(BasePage):
    """
    账套-设置-进项发票中的功能
    """

    def collect_jxfp(self):
        case_name = '采集进项发票'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.login()
            self.enter_page()
            self.click(*process_income_invoice.collect)
            self.sleep(2)
            self.click(*process_income_invoice.collect_confirm)
            self.sleep(60)
            check_info = self.check_collect()

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, case_name + '失败'

    def check_collect(self):
        n = 10
        info = None
        check_info = None
        while n > 0:
            self.sleep(10)
            try:
                self.click(*process_income_invoice.refresh_btn)
                self.sleep(5)
                info = self.get_element_text(*process_income_invoice.check_jxfp_collect)
            except Exception as why:
                pass
            print(info)
            print(info[3:6])
            if int(info[3:6]) != 0:
                check_info = True
                break

        return check_info

    def enter_page(self):
        self.page_refresh()
        self.click(*el_home_page.customer_manager_page)
        self.click(*el_business_manager.enter_btn2)
        self.sleep(2)
        self.move(*account_home.ywcl)
        self.click(*process_income_invoice.jxfp)
        self.switch_to_frame(*process_income_invoice.change_iframe)
        self.click(*process_income_invoice.refresh_btn)
        self.sleep(1)
    def create_voucher(self):
        case_name = '生成凭证'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.enter_page()
            input("正在等待您手动填写好所有发票\n如果您填写完毕请按回车键：")
            self.click(*process_income_invoice.select_all)
            self.click(*process_income_invoice.create_pz)
            self.click(*process_income_invoice.create_pz_confirm)

            check_info = self.check_data(process_income_invoice.check_pzzh, None, 2)


        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, case_name + '失败'
