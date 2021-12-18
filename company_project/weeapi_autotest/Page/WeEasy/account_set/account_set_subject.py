# !@coding  :utf-8 
# !@Time    :2021/1/7 10:35
# !@Author  :LiuLei

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_subject, account_home


class Subject(BasePage):
    """
    账套-设置-二级科目中的功能
    """
    
    def add_subject(self):
        case_name = '新增二级科目'
        print(case_name, "|开始执行")
        
        info = None
        info_list = []
        check_info = None
        n = 1
        check_subject_list = [set_subject.check_sjt1, set_subject.check_sjt2, set_subject.check_sjt3]
        
        try:
            self.enter_page_too(account_home.setting, set_subject.subject, set_subject.change_iframe)
            for i, j in zip(account_set_setting_data.subject_name, range(0, 3)):
                self.add_flow(i)
                info = self.get_element_text(*check_subject_list[j])
                if info != i:
                    break
                info_list.append(info)
            if sorted(info_list) == sorted(account_set_setting_data.subject_name):
                check_info = True
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '新增二级科目失败'
    
    def add_flow(self, subject):
        
        self.click(*set_subject.add_subject)
        self.sleep(2)
        self.send_keys(*set_subject.ipt_subject_name, subject)
        self.click(*set_subject.add_subject_confirm)
        self.sleep(1)
        self.click(*set_subject.add_confirm)
        self.sleep(3)
    
    def delete_subject(self):
        case_name = '删除二级科目'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            
            self.click(*set_subject.subject_edit)
            self.click(*set_subject.subject_delete)
            self.sleep(3)
            self.click(*set_subject.subject_delete_confirm)
            self.sleep(10)
            
            check_info = self.check_data(set_subject.check_sjt3, None)
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '删除二级科目失败'
