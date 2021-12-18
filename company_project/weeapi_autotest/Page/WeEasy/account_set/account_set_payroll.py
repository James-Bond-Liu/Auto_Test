# !@coding  :utf-8 
# !@Time    :2021/1/22 17:09
# !@Author  :LiuLei

from Page.BasePage import BasePage
from element.WeEasy.el_account_set import process_payroll, account_home
from data.config import account_set_setting_data


class PayRoll(BasePage):
    """
    薪酬表
    """
    
    def add_payroll(self):
        case_name = '新增薪酬表'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            
            self.enter_page_too(account_home.ywcl, process_payroll.payroll_page, process_payroll.change_iframe)
            
            for i in account_set_setting_data.person_register_payroll:
                self.add_payroll_flow(i)
            
            info = self.get_payroll_info()
            
            if info == account_set_setting_data.person_register_payroll_check:
                check_info = True
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def payroll_no_price_create_vouch(self):
        case_name = '薪酬表无工资数据生成凭证'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_payroll.page_refresh)
            self.click(*process_payroll.type1_create_vouch)
            
            check_info = self.check_data(process_payroll.null_price_tips, None, 2)
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def payroll_create_vouch(self):
        case_name = '薪酬表生成凭证'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_payroll.page_refresh)
            self.click(*process_payroll.type1_create_vouch)
            self.switch_to_frame(*process_payroll.vouch_iframe)
            info = self.check_data(process_payroll.vouch_total, account_set_setting_data.payroll_vouch_check[0])
            self.click(*process_payroll.vouch_save)
            self.sleep(2)
            self.switch_to_frame(*process_payroll.change_iframe)
            info2 = self.check_data(process_payroll.type1_create_vouch, account_set_setting_data.payroll_vouch_check[1],
                                    2)
            if info and info2:
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def edit_payroll_first_type(self):
        case_name = '生产经营所得-核定征收编辑人员'
        print(case_name, "|开始执行")
        
        check_info = None
        try:
            self.click(*process_payroll.page_refresh)
            self.first_type_payroll()
            info = self.get_type_info(9, 15)
            if info == account_set_setting_data.payroll_type1_check:
                check_info = True
        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def edit_payroll_second_type(self):
        case_name = '正常工资薪金表编辑人员'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_payroll.page_refresh)
            self.type_payroll(process_payroll.type2_edit, process_payroll.type2_person_edit, process_payroll.type2_list,
                              account_set_setting_data.payroll_type_data)
            info = self.get_type_info(6, 19)
            if info == account_set_setting_data.payroll_type2_check:
                check_info = True
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def edit_payroll_third_type(self):
        case_name = '外籍人员正常工资薪金编辑人员'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_payroll.page_refresh)
            self.type_payroll(process_payroll.type3_edit, process_payroll.type3_person_edit, process_payroll.type3_list,
                              account_set_setting_data.payroll_type_data)
            info = self.get_type_info(6, 13)
            if info == account_set_setting_data.payroll_type3_check:
                check_info = True
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def edit_payroll_fourth_type(self):
        case_name = ' 全年一次性奖金收入编辑人员'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_payroll.page_refresh)
            self.type_payroll(process_payroll.type4_edit, process_payroll.type4_person_edit, process_payroll.type4_list,
                              account_set_setting_data.payroll_type_data)
            info = self.get_type_info(6, 14)
            if info == account_set_setting_data.payroll_type4_check:
                check_info = True
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def edit_payroll_fifth_type(self):
        case_name = '劳务报酬(一般劳务、其他非连续劳务)'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_payroll.page_refresh)
            self.type_payroll(process_payroll.type5_edit, process_payroll.type5_person_edit, process_payroll.type5_list,
                              account_set_setting_data.payroll_type_data)
            info = self.get_type_info(7, 13)
            if info == account_set_setting_data.payroll_type5_check:
                check_info = True
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def edit_payroll_sixth_type(self):
        case_name = '劳务报酬(保险营销员、证券经纪人、其他连续劳务)'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            
            self.click(*process_payroll.page_refresh)
            self.type_payroll(process_payroll.type6_edit, process_payroll.type6_person_edit, process_payroll.type6_list,
                              account_set_setting_data.payroll_type_data)
            info = self.get_type_info(7, 14, 1)
            if info == account_set_setting_data.payroll_type6_check:
                check_info = True
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def payroll_setting(self):
        case_name = '薪酬表设置'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_payroll.page_refresh)
            self.click(*process_payroll.type2_set)
            self.select_value(*process_payroll.jsfs_setting, value='1')
            self.click(*process_payroll.setting_confirm)
            check_info = self.check_data(process_payroll.pay_method_check,
                                         account_set_setting_data.payroll_setting_check)
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def add_payroll_flow(self, select_type):
        
        self.click(*process_payroll.add_payroll)
        self.select_value(*process_payroll.compensation_type, select_type)
        try:
            self.select_value(*process_payroll.pay_method, value='2')
        except Exception as why:
            pass
        self.click(*process_payroll.save_payroll)
        self.sleep(1)
        
        if select_type == account_set_setting_data.person_register_payroll[4]:
            self.click(*process_payroll.s_add_payroll_item)
            self.click(*process_payroll.select_person)
            self.click(*process_payroll.set_zero)
            self.sleep(1)
            self.click(*process_payroll.s_return_btn)
        else:
            self.click(*process_payroll.add_payroll_item)
            self.click(*process_payroll.select_person)
            self.click(*process_payroll.set_zero)
            self.sleep(1)
            self.click(*process_payroll.return_btn)
    
    def get_payroll_info(self):
        self.sleep(2)
        info_list = []
        for i in range(1, 7):
            info = self.get_element_text('xpath', process_payroll.check_payroll % i)
            
            info_list.append(info)
        print(info_list)
        return info_list
    
    def first_type_payroll(self):
        
        self.click(*process_payroll.type1_edit)
        
        self.send_keys(*process_payroll.total_income, account_set_setting_data.payroll_type1_data[0])
        self.send_keys(*process_payroll.taxable_income, account_set_setting_data.payroll_type1_data[1], 2)
        self.sleep(1)
        self.send_keys(*process_payroll.allocation, account_set_setting_data.payroll_type1_data[2], 2)
        self.click(*process_payroll.deduction)
        self.sleep(1)
        self.send_keys(*process_payroll.endowment_insurance, account_set_setting_data.payroll_type1_data[3])
        self.send_keys(*process_payroll.medical_insurance, account_set_setting_data.payroll_type1_data[3])
        self.send_keys(*process_payroll.unemployment_insurance, account_set_setting_data.payroll_type1_data[3])
        self.send_keys(*process_payroll.provident_fund, account_set_setting_data.payroll_type1_data[3])
        self.click(*process_payroll.deduction_save)
        self.sleep(1)
        
        self.click(*process_payroll.other)
        self.sleep(1)
        self.send_keys(*process_payroll.endowment_other, account_set_setting_data.payroll_type1_data[4])
        self.send_keys(*process_payroll.deduction_other, account_set_setting_data.payroll_type1_data[4])
        self.click(*process_payroll.other_save)
        self.sleep(1)
        
        self.send_keys(*process_payroll.prepay, account_set_setting_data.payroll_type1_data[5], 2)
        self.sleep(1)
        self.click(*process_payroll.type1_payroll_save)
        self.click(*process_payroll.type1_save_confirm)
    
    def get_type_info(self, start_num, end_num, t=None):
        self.click(*process_payroll.page_refresh)
        info_list = []
        for i in range(start_num, end_num):
            info = self.get_element_text('xpath', process_payroll.check_type1 % i)
            if info == '':
                info = self.get_element_text('xpath', (process_payroll.check_type1 + '/input') % i, name='value')
            info_list.append(info)
        self.sleep(2)
        if t is None:
            self.click(*process_payroll.return_btn)
        else:
            self.click(*process_payroll.s_return_btn)
        self.sleep(1)
        print(info_list)
        return info_list
    
    def type_payroll(self, edit, person, items, data):
        self.click(*edit)
        self.sleep(0.5)
        self.click(*person)
        self.sleep(1)
        self.send_keys(*process_payroll.type_sre, data[0])
        for i in items:
            self.send_keys(*i, data[1])
        self.send_keys(*process_payroll.type_bz, data[2])
        self.click(*process_payroll.type_save)
        self.sleep(2)
