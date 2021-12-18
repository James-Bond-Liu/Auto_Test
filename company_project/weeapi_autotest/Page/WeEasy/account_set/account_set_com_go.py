# !@coding  :utf-8 
# !@Time    :2021/1/7 13:34
# !@Author  :liulei

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_come_go, account_home


class OtherComGo(BasePage):
    """
    账套-设置-其他往来中的功能
    """
    
    def add_com_go(self):
        case_name = '新增其他往来'
        print(case_name, "|开始执行")
        
        info = None
        info_list = []
        check_info = None
        n = 1
        
        try:
            self.page_refresh()
            # self.click(*el_home_page.customer_manager_page)
            # self.click(*el_business_manager.enter_btn)
            self.sleep(5)
            self.move(*account_home.setting)
            self.click(*set_come_go.com_go)
            self.switch_to_frame(*set_come_go.change_iframe)
            
            for i in account_set_setting_data.com_go_name:
                self.add_flow(i)
                check_info = self.diff_data(set_come_go.com_go_name % n, i)
                if not check_info:
                    break
                n += 1
            for i in range(1, 4):
                info = self.get_element_text('xpath', set_come_go.com_go_name % i)
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.com_go_name):
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '新增其他往来失败'
    
    def add_flow(self, costomer):
        self.click(*set_come_go.add_com_go)
        self.sleep(2)
        self.send_keys(*set_come_go.ipt_com_go_name, costomer)
        self.click(*set_come_go.add_com_go_confirm)
    
    def delete_com_go(self):
        case_name = '删除其他往来'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            # self.page_refresh()
            # self.sleep(3)
            # self.move(*el_account_set_home.setting)
            # self.click(*el_account_set_com_go.com_go)
            # self.switch_to_frame(*el_account_set_com_go.change_iframe)
            
            self.click(*set_come_go.select_box)
            self.click(*set_come_go.delete_com_go)
            self.click(*set_come_go.delete_confirm)
            self.sleep(1)

            self.check_data(set_come_go.delete_check, None)
            if info is None:
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '删除其他往来失败'
