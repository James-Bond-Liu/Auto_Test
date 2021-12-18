# !@coding  :utf-8 
# !@Time    :2021/1/7 10:35
# !@Author  :liulei

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_costomer, account_home


class Costomer(BasePage):
    """
    账套-设置-客户中的功能
    """
    
    def add_costomer(self):
        case_name = '新增客户'
        print(case_name, "|开始执行")
        
        info = None
        info_list = []
        check_info = None
        n = 1
        
        try:
            self.page_refresh()
            self.move(*account_home.setting)
            self.sleep(1)
            self.click(*set_costomer.costomer)
            self.switch_to_frame(*set_costomer.change_iframe)
            
            for i in account_set_setting_data.costomer_name:
                self.add_flow(i)
                check_info = self.diff_data(set_costomer.costomer_name % n, i)
                if not check_info:
                    break
                n += 1
            for i in range(1, 4):
                info = self.get_element_text('xpath', set_costomer.costomer_name % i)
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.costomer_name):
                check_info = True
                
        except Exception as why:
            print('why', why)
            
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '新增客户失败'
    
    def add_flow(self, costomer):
        self.click(*set_costomer.add_costomer)
        self.sleep(2)
        self.send_keys(*set_costomer.ipt_costomer_name, costomer)
        self.click(*set_costomer.add_costomer_confirm)
        self.sleep(2)
    
    def delete_costomer(self):
        case_name = '删除客户'
        print(case_name, "|开始执行")
    
        info = None
        check_info = None
    
        try:
            self.sleep(1)
            self.click(*set_costomer.select_box)
            self.click(*set_costomer.delete_costomer)
            self.click(*set_costomer.delete_confirm)
            self.sleep(1)
            
            check_info = self.check_data(set_costomer.delete_check, None)

        except Exception as why:
            print('why', why)
    
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '删除客户失败'
