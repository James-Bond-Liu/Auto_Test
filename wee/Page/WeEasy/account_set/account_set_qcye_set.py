# !@coding  :utf-8 
# !@Time    :2021/1/7 19:48
# !@Author  :LiuLei

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import set_qcye_set, account_home


class QcyeSet(BasePage):
    """
    账套-设置-期初余额设置中的功能
    """
    
    def import_qcye(self):
        case_name = '导入期初余额'
        print(case_name, "|开始执行")
        
        check_info = None
        
        try:
            self.enter_page_too(account_home.setting, set_qcye_set.qcye_set, set_qcye_set.change_iframe)
            info3 = self.get_element_text(*set_qcye_set.set_qcye_btn)
            
            self.click(*set_qcye_set.ipt_qcye)
            self.send_keys(*set_qcye_set.upload, account_set_setting_data.qcye_upload)
            self.sleep(1)
            self.click(*set_qcye_set.next_step)
            
            page_info = self.get_element_text(*set_qcye_set.check_page)
            if "为了保证会计核算的连续性，前期已有账时需设置初始余额" in page_info:
                pass
            else:
                print('================================================='
                      '======================================================')
                assert False, '新增期初余额设置失败'
            self.sleep(10)
            self.click(*set_qcye_set.ssph_btn)
            
            info = self.get_element_text(*set_qcye_set.get_ssph_info)
            info1 = self.get_element_text(*set_qcye_set.get_ssph_info2)
            print(info)
            print(info1)
            self.click(*set_qcye_set.close_ssph)
            self.sleep(2)
            self.click(*set_qcye_set.save_btn)
            
            info3 = self.check_data(set_qcye_set.set_qcye_btn, account_set_setting_data.qcye_check3)
            
            if info == account_set_setting_data.qcye_check and info1 == account_set_setting_data.qcye_check2 and info3:
                check_info = True
        
        except Exception as why:
            print('why', why)
        #
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '新增期初余额设置失败'
    
    def clear_qcye(self):
        case_name = '清空期初余额设置'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*set_qcye_set.set_qcye_btn)
            self.click(*set_qcye_set.clear_data)
            self.sleep(2)
            self.click(*set_qcye_set.clear_confirm)
            self.sleep(10)
            info = self.get_element_text(*set_qcye_set.clear_success)
            print(info)
            if info == account_set_setting_data.qcye_check_clear_info:
                check_info = True
        
        except Exception as why:
            print('why', why)
        #
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '新增期初余额设置失败'
