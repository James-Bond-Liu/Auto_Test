# !@coding  :utf-8 
# !@Time    :2021/1/11 16:17
# !@Author  :liulei

from Page.BasePage import BasePage
from element.WeEasy import el_business_manager
from element.WeEasy import el_home_page
from element.WeEasy.el_account_set import statement_swbb, account_home


class Swbb(BasePage):

    def qushu(self):
        case_name = '税务报表取数'
        print(case_name, "|开始执行")

        check_info = None
        info = None

        self.login()
        self.enter_page()
        try:
            for i in range(1, 4):
                info = self.get_qs_data(statement_swbb.qushu % i,
                                        statement_swbb.sk % i)
                print('1111')
        except Exception as why:
            print(why)
        if info:
            check_info = True

        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, case_name + '失败'

    def get_qs_data(self, qs, sk):
        info = None
        sk_info = None
        check_info = None
        self.click('xpath', qs)

        info = self.check_data(statement_swbb.check_tips, '取数成功')
        sk_info = self.check_data(('xpath', sk), None, 2)
        print(sk_info)

        if info and sk_info:
            check_info = True
        return check_info

    def enter_page(self):
        self.page_refresh()
        self.click(*el_home_page.customer_manager_page)
        self.click(*el_business_manager.enter_btn2)
        self.sleep(2)
        self.page_refresh()
        self.move(*account_home.bb)
        self.click(*statement_swbb.swbb)
        self.switch_to_frame(*statement_swbb.change_iframe)

    def shenbao(self):
        case_name = '税务申报'
        print(case_name, "|开始执行")

        check_info = None
        try:
            self.login()
            self.enter_page()
            self.click(*statement_swbb.page_refresh)
            self.click(*statement_swbb.select_all)

            self.click(*statement_swbb.sb)
            self.sleep(1)
            self.click(*statement_swbb.sb_confim)

            self.sleep(60)
            check_info = self.get_shenbao_status()

        except Exception as why:
            print(why)
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, case_name + '失败'

    def get_shenbao_status(self):
        info = None
        for i in range(1, 2):
            info = self.check_data(('xpath', statement_swbb.sb_status % i), '未申报 ', 2)
            print(info)
            if info:
                return info
            else:
                info = False
                return info
