# !@coding  :utf-8 
# !@Time    :2021/1/7 14:36
# !@Author  :liulei


from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_product, account_home


class Product(BasePage):
    """
    账套-设置-项目中的功能
    """
    
    def add_product(self):
        case_name = '新增项目'
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
            self.click(*set_product.product)
            self.switch_to_frame(*set_product.change_iframe)
            
            for i in account_set_setting_data.product_name:
                self.add_flow(i)
                check_info = self.diff_data(set_product.product_name % n, i)
                if not check_info:
                    break
                n += 1
            for i in range(1, 4):
                info = self.get_element_text('xpath', set_product.product_name % i)
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.product_name):
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '新增项目失败'
    
    def add_flow(self, costomer):
        self.click(*set_product.add_product)
        self.sleep(2)
        self.send_keys(*set_product.ipt_product_name, costomer)
        self.click(*set_product.add_product_confirm)
    
    def delete_product(self):
        case_name = '删除项目'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            # self.page_refresh()
            # self.sleep(3)
            # self.move(*el_account_set_home.setting)
            # self.click(*el_account_set_product.product)
            # self.switch_to_frame(*el_account_set_product.change_iframe)
            
            self.click(*set_product.select_box)
            self.click(*set_product.delete_product)
            self.click(*set_product.delete_confirm)
            self.sleep(1)

            check_info = self.check_data(set_product.delete_check, None)

        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, '删除项目失败'
