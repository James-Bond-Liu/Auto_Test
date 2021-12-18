# !@coding  :utf-8 
# !@Time    :2021/1/28 16:42
# !@Author  :LiuLei
from Page.BasePage import BasePage
from element.WeEasy.el_account_set import process_deprecition, account_home
from data.config import account_set_setting_data


class Deprecition(BasePage):
    """
    账套-业务处理-折旧摊销
    """
    
    def add_deprecition_item(self):
        
        case_name = '折旧摊销-添加资产'
        print(case_name, "|开始执行")
        
        info_list = []
        check_info = None
        
        try:
            self.enter_page_too(account_home.ywcl, process_deprecition.deprecition_page,
                                process_deprecition.change_iframe)
            self.click(*process_deprecition.add_asset)
            self.select_value(*process_deprecition.asset_type, '01')
            for i, j in zip(process_deprecition.asset_list, account_set_setting_data.deprecition):
                self.send_keys(*i, j)
            self.click(*process_deprecition.asset_save_btn)
            self.click(*process_deprecition.asset_ignore)
            self.sleep(1)
            for i in range(3, 13):
                info = self.get_element_text('xpath', process_deprecition.first_item_check % i)
                info_list.append(info)
            print(info_list)
            if info_list == account_set_setting_data.deprecition_check:
                check_info = True
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def edit_deprecition(self):
        case_name = '折旧摊销-编辑资产'
        print(case_name, "|开始执行")
        
        info_list = []
        
        check_info = None
        try:
            self.click(*process_deprecition.page_refresh)
            self.click(*process_deprecition.asset_detail)
            self.sleep(1)
            self.click(*process_deprecition.asset_edit)
            
            for i, j in zip(process_deprecition.asset_list, account_set_setting_data.deprecition_edit):
                self.send_keys(*i, j)
                self.sleep(0.5)
            self.click(*process_deprecition.asset_save_btn)
            self.click(*process_deprecition.asset_ignore)
            for i in range(3, 13):
                info = self.get_element_text('xpath', process_deprecition.first_item_check % i)
                info_list.append(info)
            print(info_list)
            if info_list == account_set_setting_data.deprecition_edit_check:
                check_info = True
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def delete_depercition(self):
        case_name = '折旧摊销-删除资产'
        print(case_name, "|开始执行")
        
        check_info = None
        try:
            self.click(*process_deprecition.page_refresh)
            self.click(*process_deprecition.first_item_select_box)
            self.click(*process_deprecition.delete_asset)
            self.sleep(1)
            self.click(*process_deprecition.delete_confirm)
            check_info = self.check_data(process_deprecition.check_page, None)
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
