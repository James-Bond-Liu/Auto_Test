# !@coding  :utf-8 
# !@Time    :2021/1/20 11:05
# !@Author  :LiuLei
from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import process_people_register, account_home


class PeopleRegister(BasePage):
    """

    业务处理-人员登记

    """
    
    def add_cisborder_person(self):
        case_name = '新增境内人员登记'
        print(case_name, "|开始执行")
        
        info = None
        
        check_info = None
        
        try:
            # self.login()
            self.enter_page_too(account_home.ywcl, process_people_register.people_register,
                                process_people_register.change_iframe)
            self.add_flow(person_type=process_people_register.add_cisborder_person, status='0',
                          identity=account_set_setting_data.person_register_identity_card[0],
                          name=account_set_setting_data.person_register_name[0], sex='1', partner='1',
                          phone=account_set_setting_data.person_register_phone[0])
            
            self.switch_to_frame(*process_people_register.change_iframe)
            info1 = self.check_data(process_people_register.last_person_check,
                                    account_set_setting_data.person_register_name[0])
            
            self.add_flow(person_type=process_people_register.add_cisborder_person, status='1',
                          identity=account_set_setting_data.person_register_identity_card[1],
                          name=account_set_setting_data.person_register_name[1], sex='1', partner='0',
                          phone=account_set_setting_data.person_register_phone[1])
            self.switch_to_frame(*process_people_register.change_iframe)
            info2 = self.check_data(process_people_register.last_person_check,
                                    account_set_setting_data.person_register_name[1])
            if info1 and info2:
                check_info = True
        except Exception as why:
            print('why', why)
            print('添加人员失败')
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def add_overseas_person(self):
        case_name = '新增境外人员登记'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_people_register.page_refresh)
            self.add_flow(person_type=process_people_register.add_overseas_person, status='0',
                          identity=account_set_setting_data.person_register_identity_card[2],
                          name=account_set_setting_data.person_register_name[2], sex='1', partner='0',
                          phone=account_set_setting_data.person_register_phone[2])
            self.switch_to_frame(*process_people_register.change_iframe)
            check_info = self.check_data(process_people_register.last_person_check,
                                         account_set_setting_data.person_register_name[2])
        except Exception as why:
            print('添加人员失败')
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def batch_edit(self):
        case_name = '批量编辑人员登记'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        element_list = [process_people_register.nsrzt_date, process_people_register.person_type,
                        process_people_register.money_type]
        
        try:
            self.click(*process_people_register.page_refresh)
            for i, j, k in zip(account_set_setting_data.person_register_edit, element_list,
                               account_set_setting_data.person_register_edit_value):
                self.edit_flow(edit=i, select_type=j, type_value=k)
            info = self.get_edit_info()
            self.sleep(1)
            self.click(*process_people_register.last_person_edit)
            self.click(*process_people_register.edit_person)
            self.select_value(*process_people_register.edit_property, account_set_setting_data.person_register_edit[1])
            self.select_value(*process_people_register.person_type, '10')
            self.click(*process_people_register.edit_save)
            self.sleep(2)
            if info == account_set_setting_data.person_register_edit_check:
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def delete_person(self):
        case_name = '删除人员登记'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            
            self.click(*process_people_register.page_refresh)
            self.click(*process_people_register.second_person_delete)
            self.click(*process_people_register.delete_person)
            self.click(*process_people_register.delete_confirm)
            self.click(*process_people_register.page_refresh)
            
            check_info = self.check_data(process_people_register.second_person_check,
                                         account_set_setting_data.person_register_name[2])
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def import_person(self):
        case_name = '导入人员'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            
            self.click(*process_people_register.page_refresh)
            self.click(*process_people_register.import_menu)
            self.click(*process_people_register.import_btn)
            self.sleep(2)
            self.send_keys(*process_people_register.choose_file, account_set_setting_data.person_register_data)
            self.click(*process_people_register.upload_btn)
            
            check_info = self.check_data(process_people_register.import_tips,
                                         account_set_setting_data.person_register_import)
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def add_flow(self, person_type, status, identity, name, sex, partner, phone):
        """新增人员的流程"""
        # self.switch_to_frame(*process_people_register.change_iframe)
        self.click(*person_type)
        self.select_value(*process_people_register.person_status, status)
        self.send_keys(*process_people_register.person_identity_card, identity)
        self.send_keys(*process_people_register.person_name, name)
        self.select_value(*process_people_register.person_sex, value=sex)
        self.send_keys(*process_people_register.dimission_date, account_set_setting_data.person_register_dimission)
        self.select_value(*process_people_register.partner_status, partner)
        self.send_keys(*process_people_register.person_phone, phone)
        
        if person_type == process_people_register.add_overseas_person:
            self.send_keys(*process_people_register.person_birth, value=account_set_setting_data.person_register_birth)
            self.click(*process_people_register.save_btn)
            self.sleep(0.2)
            self.click(*process_people_register.person_nationality)
            self.sleep(0.3)
            self.click(*process_people_register.select_nationality)
            self.sleep(0.3)
            self.click(*process_people_register.person_birth_place)
            self.sleep(0.3)
            self.click(*process_people_register.select_birth_place)
            
            self.send_keys(*process_people_register.first_inbound, value='2019-01-03')
            self.send_keys(*process_people_register.departure, value='2021-01-20')
            self.click(*process_people_register.reason)
            self.sleep(0.3)
            self.click(*process_people_register.select_reason)
        
        self.click(*process_people_register.save_btn)
        self.sleep(1)
        log = False
        try:
            self.click(*process_people_register.tips_confirm)
            log = True
        except Exception as why:
            print('tips_confirm不存在')
            self.click(*process_people_register.save_continue)
        if log:
            self.click(*process_people_register.save_continue)
        self.sleep(2)
    
    def edit_flow(self, edit, select_type, type_value):
        self.click(*process_people_register.select_all)
        self.click(*process_people_register.edit_person)
        self.sleep(0.5)
        self.select_value(*process_people_register.edit_property, edit)  # 修改人员状态
        
        if edit == account_set_setting_data.person_register_edit[0]:
            self.send_keys(*select_type, type_value)
            self.click(*process_people_register.edit_property)
            self.click(*process_people_register.edit_save)
            self.click(*process_people_register.tips_save)
        elif edit == account_set_setting_data.person_register_edit[1]:
            self.select_value(*select_type, type_value)
            self.click(*process_people_register.edit_save)
        
        elif edit == account_set_setting_data.person_register_edit[2]:
            self.select_text(*select_type, type_value)
            self.click(*process_people_register.edit_save)
        self.sleep(2)
    
    def get_edit_info(self):
        info = []
        for i in range(1, 4):
            a = []
            for j in range(8, 11):
                data = self.get_element_text('xpath', process_people_register.edit_check % (i, j))
                a.append(data)
            info.append(a)
        return info
