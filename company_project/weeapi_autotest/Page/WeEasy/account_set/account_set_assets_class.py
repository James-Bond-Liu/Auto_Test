# !@coding  :utf-8 
# !@Time    :2021/1/7 14:36
# !@Author  :liulei


from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_assets_class, account_home


class AssetsClass(BasePage):
    """
    账套-设置-资产类别中的功能
    """
    
    def add_assets_class(self):
        case_name = '新增资产类别'
        print(case_name, "|开始执行")
        
        info = None
        info_list = []
        check_info = None
        n = 1
        
        try:
            self.page_refresh()
            # self.click(*el_home_page.customer_manager_page)
            # self.click(*el_business_manager.enter_btn)
            self.sleep(2)
            self.move(*account_home.setting)
            self.click(*set_assets_class.assets_class)
            self.switch_to_frame(*set_assets_class.change_iframe)
            
            for i in account_set_setting_data.assets_class:
                self.add_flow(i)
                check_info = self.diff_data(set_assets_class.assets_class_name % n, i[1])
                if not check_info:
                    break
                n += 1
            for i in range(1, 4):
                info = self.get_element_text('xpath', set_assets_class.assets_class_name % i)
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.assets_class):
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '新增资产类别失败'
    
    def add_flow(self, costomer):
        self.click(*set_assets_class.add_assets_class)
        self.sleep(2)
        self.send_keys(*set_assets_class.ipt_assets_class_num, costomer[0])

        self.send_keys(*set_assets_class.ipt_assets_class_name, costomer[1])
        
        self.click(*set_assets_class.ipt_swzclb)
        self.click(*set_assets_class.select_swzclb)

        self.send_keys(*set_assets_class.ipt_s_synx, costomer[2])

        self.send_keys(*set_assets_class.ipt_s_czl, costomer[3])
        
        self.click(*set_assets_class.add_assets_class_confirm)
    
    def delete_assets_class(self):
        case_name = '删除资产类别'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            # self.page_refresh()
            # self.sleep(3)
            # self.move(*el_account_set_home.setting)
            # self.click(*el_account_set_assets_class.assets_class)
            # self.switch_to_frame(*el_account_set_assets_class.change_iframe)
            self.click(*set_assets_class.refresh_page)
            self.click(*set_assets_class.select_box)
            self.click(*set_assets_class.delete_assets_class)
            self.click(*set_assets_class.delete_confirm)
            self.sleep(1)
            check_info = self.check_data(set_assets_class.delete_check, None)

        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '删除资产类别失败'
