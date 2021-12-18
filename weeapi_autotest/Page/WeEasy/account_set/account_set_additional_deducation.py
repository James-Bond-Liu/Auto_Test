# !@coding  :utf-8 
# !@Time    :2021/1/25 16:22
# !@Author  :liulei

from Page.BasePage import BasePage
from element.WeEasy.el_account_set import process_additional_deduction, account_home
from data.config import account_set_setting_data


class AdditionalDeducation(BasePage):
    """
    账套-业务处理-专项附加扣除
    """

    def children_education_add_child(self):

        case_name = '子女教育支出-登记子女'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:

            self.enter_page_too(account_home.ywcl, process_additional_deduction.payroll_page,
                                process_additional_deduction.change_iframe)
            for i in process_additional_deduction.child_list:
                self.click(*i)
            self.send_keys(*process_additional_deduction.child_name,
                           account_set_setting_data.additonal_deduction_children[0])
            self.select_value(*process_additional_deduction.child_identity_type, value='201')
            self.send_keys(*process_additional_deduction.child_identity_card,
                           account_set_setting_data.additonal_deduction_children[1])
            self.select_value(*process_additional_deduction.state_chosen, value='156')
            self.select_value(*process_additional_deduction.child_education_type_chosen, value='40')
            self.send_keys(*process_additional_deduction.start_education,
                           account_set_setting_data.additonal_deduction_children[2])
            self.select_value(*process_additional_deduction.attend_country, value='156')
            self.send_keys(*process_additional_deduction.attend_school,
                           account_set_setting_data.additonal_deduction_children[3])
            self.click(*process_additional_deduction.save_btn)

            check_info = self.check_data(process_additional_deduction.check_add,
                                         account_set_setting_data.additonal_deduction_children_check)
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def continuew_deucation(self):
        case_name = '继续教育支出'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.click(*process_additional_deduction.page_refresh)
            self.click(*process_additional_deduction.continue_education)
            for i in process_additional_deduction.child_list:
                self.click(*i)
            self.select_value(*process_additional_deduction.con_educa_type, value='21')
            self.sleep(1)

            for i, j in zip(process_additional_deduction.edu_list,
                            account_set_setting_data.additonal_deduction_continue_education):
                self.send_keys(*i, j)
            self.select_value(*process_additional_deduction.con_educa_name, value='20401')
            self.click(*process_additional_deduction.save_btn)

            check_info = self.check_data(process_additional_deduction.check_add,
                                         account_set_setting_data.additonal_deduction_children_check)
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def housing_loans(self):
        case_name = '住房贷款利息支出'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.click(*process_additional_deduction.page_refresh)
            self.click(*process_additional_deduction.housing_loans)
            self.click(*process_additional_deduction.add_btn)
            self.click(*process_additional_deduction.xm_chosen)
            self.click(*process_additional_deduction.select_xm)
            self.select_value(*process_additional_deduction.house_type, value='01')
            self.sleep(1)
            for i, j in zip(process_additional_deduction.house_list,
                            account_set_setting_data.additonal_deduction_housing_loans):
                self.send_keys(*i, j)
            self.click(*process_additional_deduction.save_btn)
            check_info = self.check_data(process_additional_deduction.check_add,
                                         account_set_setting_data.additonal_deduction_children_check)
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def house_rents(self):
        case_name = '住房租金支出'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:

            self.click(*process_additional_deduction.page_refresh)
            self.click(*process_additional_deduction.housing_rents)
            self.sleep(1)

            for i in process_additional_deduction.house:
                self.click(*i)
            self.select_value(*process_additional_deduction.lessor_type, value='0')

            for i, j in zip(process_additional_deduction.house_rents_list,
                            account_set_setting_data.additonal_deduction_house_rents):
                self.send_keys(*i, j)

            self.click(*process_additional_deduction.save_btn)
            check_info = self.check_data(process_additional_deduction.check_add,
                                         account_set_setting_data.additonal_deduction_children_check)
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def care_old(self):
        case_name = '赡养老人支出'
        print(case_name, "|开始执行")

        info = None
        check_info = None
        value_list = ['3', '201', '156', '5']
        try:
            self.click(*process_additional_deduction.page_refresh)
            self.click(*process_additional_deduction.care_old)
            self.sleep(1)
            for i in process_additional_deduction.older_list:
                self.click(*i)
            for i, j in zip(process_additional_deduction.older_select, value_list):
                self.select_value(*i, j)
            for i, j in zip(process_additional_deduction.older_send,
                            account_set_setting_data.additonal_deduction_care_old):
                self.send_keys(*i, j)

            self.click(*process_additional_deduction.save_btn)
            check_info = self.check_data(process_additional_deduction.check_add,
                                         account_set_setting_data.additonal_deduction_children_check)
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
