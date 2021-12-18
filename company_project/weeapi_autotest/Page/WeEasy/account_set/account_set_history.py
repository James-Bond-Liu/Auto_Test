# !@coding  :utf-8 
# !@Time    :2021/1/7 10:35
# !@Author  :LiuLei

import os

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import process_history, account_home


class History(BasePage):
    """
    账套-设置-历史凭证

    """
    def import_history(self):
        case_name = '导入历史凭证'
        print(case_name, "|开始执行")
        info = None
        info_list = []
        check_info = None
        n = 1

        try:
            self.page_refresh()
            self.sleep(5)
            self.move(*account_home.setting)
            self.click(*process_history.history)
            self.switch_to_frame(*process_history.change_iframe)

            self.click(*process_history.history_import)

            self.auto_upload(file=account_set_setting_data.history_data)
            
            self.check_data(process_history.check_import_status, account_set_setting_data.history_import_status)
            self.sleep(10)
            info = self.get_element_text(*process_history.check_data)
            if info == account_set_setting_data.history_check_import:
                check_info = True

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, case_name + '失败'

    def delete_history(self):
        case_name = '删除历史凭证'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.page_refresh()
            self.sleep(5)
            self.move(*account_home.setting)
            self.click(*process_history.history)
            self.switch_to_frame(*process_history.change_iframe)

            self.click(*process_history.select_box)
            self.click(*process_history.delete_history)
            self.click(*process_history.delete_confirm)
            self.sleep(10)

            info = self.get_element_text(*process_history.check_data)
            if info == account_set_setting_data.history_check_delete:
                check_info = True

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print(
            '=======================================================================================================')
        assert result_status, case_name + '失败'
