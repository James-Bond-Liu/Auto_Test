# !@coding  :utf-8 
# !@Time    :2021/1/7 14:36
# !@Author  :liulei


from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_sections, account_home


class Sections(BasePage):
    """
    账套-设置-部门中的功能
    """
    
    def add_sections(self):
        case_name = '新增部门'
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
            self.click(*set_sections.sections)
            self.switch_to_frame(*set_sections.change_iframe)
            
            for i in account_set_setting_data.sections_name:
                self.add_flow(i)
                check_info = self.diff_data(set_sections.sections_name % n, i)
                if not check_info:
                    break
                n += 1
            for i in range(1, 4):
                info = self.get_element_text('xpath', set_sections.sections_name % i)
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.sections_name):
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '新增部门失败'
    
    def add_flow(self, costomer):
        self.click(*set_sections.add_sections)
        self.sleep(2)
        self.send_keys(*set_sections.ipt_sections_name, costomer)
        self.click(*set_sections.add_sections_confirm)
    
    def delete_sections(self):
        case_name = '删除部门'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            # self.page_refresh()
            # self.sleep(3)
            # self.move(*el_account_set_home.setting)
            # self.click(*el_account_set_sections.sections)
            # self.switch_to_frame(*el_account_set_sections.change_iframe)
            
            self.click(*set_sections.delete_sections)
            alert = self.switch_alert()
            alert.accept()
            self.sleep(1)

            check_info = self.check_data(set_sections.delete_check, None)

        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '删除部门失败'
