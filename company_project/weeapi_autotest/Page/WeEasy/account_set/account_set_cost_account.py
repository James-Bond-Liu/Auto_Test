# !@coding  :utf-8 
# !@Time    :2021/4/2 21:29
# !@Author  :LiuLei
"""成本核算"""

from Page.BasePage import BasePage
from element.WeEasy.el_account_set import process_cost_account, account_home
from data.config import account_set_setting_data


class CostAccount(BasePage):
    
    @BasePage._base
    def proccess_cost_account(self):
        case_name = '成本核算'
        print(case_name, "|开始执行")
        check_info = False
        check_list = []
        # self.login()
        self.enter_page_too(account_home.ywcl, process_cost_account.cost, process_cost_account.change_iframe)
        self.click(*process_cost_account.sccbhs)
        self.click(*process_cost_account.rest_save)
        self.sleep(1)
        self.click(*process_cost_account.cost_confirm)
        self.sleep(1)
        for i in range(4):
            self.click(*process_cost_account.next_step)
            self.sleep(0.5)
        info = self.get_element_text(*process_cost_account.last_tips)
        if info == '生成出入库单成功！':
            self.click(*process_cost_account.choose_product)
            self.sleep(1)
            for i in range(1, 3):
                self.click('xpath', process_cost_account.select_product % i)
            self.click(*process_cost_account.select_confirm)
            self.send_keys(*process_cost_account.apportion, account_set_setting_data.cost_data[0])
            for i in range(1, 3):
                self.send_keys('xpath', process_cost_account.ipt_num % i, account_set_setting_data.cost_data[1])
            self.click(*process_cost_account.cost_completed)
            self.sleep(2)
        else:
            return check_info, case_name
        for i in range(7, 14):
            info = self.get_element_text('xpath', process_cost_account.check_data % i)
            check_list.append(info)
        info = self.get_element_text(*process_cost_account.check_info)
        if check_list == account_set_setting_data.cost_check_data and info == account_set_setting_data.cost_check_info:
            check_info = True
        return check_info, case_name
