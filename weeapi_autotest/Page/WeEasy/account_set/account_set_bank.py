# !@coding  :utf-8 
# !@Time    :2021/1/6 15:26
# !@Author  :liulei

from Page.BasePage import BasePage
from data.config import account_set_setting_data,login_data
from element.WeEasy import el_business_manager
from element.WeEasy import el_home_page
from element.WeEasy.el_account_set import set_account_register, account_home


class AccountSet(BasePage):
    """
    账套功能-银行账户
    """
    
    def add_account(self):
        case_name = '新增银行账户'
        print(case_name, "|开始执行")
        info = None
        info_list = []
        check_info = None
        bank_list = [set_account_register.bank_type1, set_account_register.bank_type2,
                     set_account_register.bank_type3]
        
        try:
            self.load_url(login_data.login_url)
            self.click(*el_home_page.customer_manager_page)
            self.click(*el_business_manager.enter_btn)
            self.sleep(5)
            self.move(*account_home.setting)
            self.click(*set_account_register.zhdj)
            self.switch_to_frame(*set_account_register.change_iframe)
            
            for i, j in zip(bank_list, account_set_setting_data.bank_name):
                self.add_acc(i, j)
            
            for i in range(1, 4):
                info = self.get_element_text(set_account_register.get_bank_name1, set_account_register.get_bank_name2 % i)
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.bank_name):
                check_info = True
            else:
                check_info = False

        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '新增银行账户失败'
    
    def add_acc(self, bank, bank_name):
        self.click(*set_account_register.add_account)
        self.click(*set_account_register.ipt_bank)
        self.click(*bank)
        
        self.clear(*set_account_register.account_num)
        self.send_keys(*set_account_register.account_num, account_set_setting_data.bank_num)
        
        self.clear(*set_account_register.account_name)
        self.send_keys(*set_account_register.account_name, bank_name)
        self.click(*set_account_register.save)
        self.sleep(2)
        self.check_data(set_account_register.add_account, '新建账户')

    def delete_account(self):
        case_name = '删除银行账户'
        print(case_name, "|开始执行")
        
        check_info = None
        info = None
        
        try:
            # self.page_refresh()
            # self.move(*el_account_set_home.setting)
            # self.click(*el_account_set_zhdj.zhdj)
            # self.switch_to_frame(*el_account_set_zhdj.change_iframe)
            #
            self.click(*set_account_register.delete_btn)
            confirm = self.switch_alert()
            confirm.accept()
            self.sleep(1)

            check_info = self.check_data(set_account_register.delete_bank_info, None)

        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '删除银行账户失败'
