# !@coding  :utf-8 
# !@Time    :2021/1/7 14:36
# !@Author  :liulei

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_tags, account_home


class Tags(BasePage):
    """
    账套-设置-标签中的功能
    """
    
    def add_tags(self):
        case_name = '新增标签'
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
            self.click(*set_tags.tags)
            self.switch_to_frame(*set_tags.change_iframe)
            
            for i in account_set_setting_data.tags_name:
                self.add_flow(i)
                check_info = self.diff_data(set_tags.tags_name % n, i)
                if not check_info:
                    break
                n += 1
            for i in range(1, 4):
                info = self.get_element_text('xpath', set_tags.tags_name % i)
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.tags_name):
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '新增标签失败'
    
    def add_flow(self, costomer):
        self.click(*set_tags.add_tags)
        self.sleep(2)
        self.send_keys(*set_tags.ipt_tags_name, costomer)
        self.click(*set_tags.add_tags_confirm)
    
    def delete_tags(self):
        case_name = '删除标签'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            # self.page_refresh()
            # self.sleep(3)
            # self.move(*el_account_set_home.setting)
            # self.click(*el_account_set_tags.tags)
            # self.switch_to_frame(*el_account_set_tags.change_iframe)
            #
            self.click(*set_tags.select_box)
            self.click(*set_tags.delete_tags)
            self.click(*set_tags.delete_confirm)
            self.sleep(1)

            check_info = self.check_data(set_tags.delete_check, None)

        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '删除标签失败'
