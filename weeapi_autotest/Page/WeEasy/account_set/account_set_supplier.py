# !@coding  :utf-8 
# !@Time    :2021/1/7 13:34
# !@Author  :liulei


from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_supplier, account_home


class Supplier(BasePage):
    """
    账套-设置-供应商中的功能
    """
    
    def add_supplier(self):
        case_name = '新增供应商'
        print(case_name, "|开始执行")
        
        info = None
        info_list = []
        check_info = None
        n = 1
        
        try:
            self.page_refresh()
            self.sleep(5)
            self.move(*account_home.setting)
            self.click(*set_supplier.supplier)
            self.switch_to_frame(*set_supplier.change_iframe)
            
            for i in account_set_setting_data.supplier_name:
                self.add_flow(i)
                check_info = self.diff_data(set_supplier.supplier_name % n, i)
                if not check_info:
                    break
                n += 1
            for i in range(1, 4):
                info = self.get_element_text('xpath', set_supplier.supplier_name % i)
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.supplier_name):
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '新增供应商失败'
    
    def add_flow(self, costomer):
        self.click(*set_supplier.add_supplier)
        self.sleep(2)
        self.send_keys(*set_supplier.ipt_supplier_name, costomer)
        self.click(*set_supplier.add_supplier_confirm)
    
    def delete_supplier(self):
        case_name = '删除供应商'
        print(case_name, "|开始执行")

        check_info = None
        
        try:
            self.click(*set_supplier.select_box)
            self.click(*set_supplier.delete_supplier)
            self.click(*set_supplier.delete_confirm)
            self.sleep(1)

            check_info = self.check_data(set_supplier.delete_check, None)

        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '删除供应商失败'
