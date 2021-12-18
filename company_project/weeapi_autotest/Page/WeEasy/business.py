# !@coding  :utf-8 
# !@Time    :2021/1/5 20:47
# !@Author  :LiuLei
from Page.BasePage import BasePage
from data.config import business_data
from data.config import login_data
from element.WeEasy import el_business_manager
from element.WeEasy import el_home_page


class BusinessManager(BasePage):
    """
    企业管理界面
    """

    def add_business(self):
        case_name = "添加企业"
        print(case_name, "|开始执行")

        check = None
        check_info = None

        try:
            self.page_refresh()
            self.click(*el_home_page.customer_manager_page)

            for i in business_data.business_list:
                self.add_flow(i)
                check_info = self.diff_data(el_business_manager.first_business_name, i)
                self.page_refresh()
                if not check_info:
                    break
            print('所有企业添加完毕')

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '添加企业失败'

    def add_flow(self, business):
        self.click(*el_business_manager.add_business)
        self.sleep(1)
        self.select_value(*el_business_manager.select_province, business_data.business_province)
        self.select_value(*el_business_manager.select_city, business_data.business_city)
        self.send_keys(*el_business_manager.ipt_business_name, business)
        self.send_keys(*el_business_manager.identity_num, business_data.business_num)
        self.send_keys(*el_business_manager.telephone_num, business_data.business_num)
        self.send_keys(*el_business_manager.gssb_pwd, business_data.business_num)
        self.click(*el_business_manager.save_btn)

    def delete_business(self):
        case_name = "删除企业"
        print(case_name, "|开始执行")

        check_info = None
        info = None
        try:
            self.page_refresh()
            self.click(*el_business_manager.business_name5_delete)
            self.sleep(1)
            self.clear(*el_business_manager.ipt_delete_pwd)
            self.send_keys(*el_business_manager.ipt_delete_pwd, login_data.password)
            self.click(*el_business_manager.delete_confirm)
            self.click(*el_business_manager.s_delete_btn)
            self.sleep(2)
            check_info = self.check_data(el_business_manager.business_name5, None)

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '删除企业失败'

    def block_business(self):
        case_name = "停用企业"
        print(case_name, "|开始执行")

        check_info = None
        info = None
        try:
            self.page_refresh()
            self.click(*el_business_manager.business_name4_block_btn)
            self.sleep(2)
            self.click(*el_business_manager.s_block_btn)

            self.click(*el_business_manager.block_filter)

            info = self.get_element_text(*el_business_manager.business_name4)
            if info == business_data.business_list[3]:
                check_info = True
            self.sleep(2)
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '停用企业失败'

    def batch_block_business(self):
        case_name = "批量停用企业"
        print(case_name, "|开始执行")

        check_info = None
        info = None
        business_list = [el_business_manager.business_name1, el_business_manager.business_name2,
                         el_business_manager.business_name3, el_business_manager.business_name4]
        check_business = []
        try:

            self.click(*el_business_manager.normal_filter)
            self.click(*el_business_manager.select_all_business)
            self.sleep(1)
            self.click(*el_business_manager.batch_block_btn)
            n = 10
            while n > 0:
                wait = self.get_element_text(*el_business_manager.s_batch_block_btn, name='value')
                if wait == '停用':
                    break
                self.sleep(1)
                n -= 1
                print(wait)
            self.click(*el_business_manager.s_batch_block_btn)
            self.page_refresh()
            self.click(*el_business_manager.block_filter)
            self.page_refresh()
            for i in business_list:
                info = self.get_element_text(*i)
                check_business.append(info)
            print(check_business)
            if sorted(check_business) == sorted(business_data.business_list[0:4]):
                check_info = True

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '批量停用企业失败'

    def batch_unblock_business(self):
        case_name = "批量启用企业"
        print(case_name, "|开始执行")

        check_info = None
        info = None
        business_list = [el_business_manager.business_name1, el_business_manager.business_name2,
                         el_business_manager.business_name3, el_business_manager.business_name4]
        check_business = []
        try:
            self.page_refresh()
            self.click(*el_business_manager.block_filter)
            self.click(*el_business_manager.select_all_business)
            self.sleep(1)
            self.click(*el_business_manager.batch_unblock_btn)
            self.sleep(2)
            self.click(*el_business_manager.s_batch_unblock_btn)
            self.click(*el_business_manager.normal_filter)
            self.page_refresh()
            for i in business_list:
                info = self.get_element_text(*i)
                check_business.append(info)
            if sorted(check_business) == sorted(business_data.business_list[0:4]):
                check_info = True

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '批量启用企业失败'

    def batch_delete_business(self):
        case_name = "批量删除企业"
        print(case_name, "|开始执行")

        check_info = None
        info = None

        try:
            self.page_refresh()
            self.click(*el_business_manager.normal_filter)
            self.click(*el_business_manager.select_all_business)
            self.sleep(1)
            self.click(*el_business_manager.select_this)
            self.sleep(1)
            self.click(*el_business_manager.batch_delete_btn)
            self.sleep(2)
            self.clear(*el_business_manager.ipt_delete_pwd)
            self.send_keys(*el_business_manager.ipt_delete_pwd, login_data.password)
            self.click(*el_business_manager.delete_confirm)
            self.sleep(2)
            self.click(*el_business_manager.s_delete_btn)
            self.page_refresh()

            check_info = self.check_data(('xpath', el_business_manager.first_business_name),
                                         business_data.business_list[0])

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '批量删除企业失败'

    def add_last_name(self):
        case_name = "新增企业曾用名"
        print(case_name, "|开始执行")

        check_info = None
        info = None
        try:
            self.page_refresh()
            self.click(*el_business_manager.business_name1_edit)
            self.sleep(2)
            self.click(*el_business_manager.business_last_name)
            self.sleep(2)
            for i in business_data.business_last_name:
                self.click(*el_business_manager.business_add_last_name)
                self.send_keys(*el_business_manager.business_ipt_cym_mc, i)
                self.click(*el_business_manager.business_save)

            check_info = self.check_data(el_business_manager.business_check_last_name,
                                         business_data.business_last_name[0])

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def change_business_open_time(self):
        case_name = "配置企业环境"
        print(case_name, "|开始执行")

        check_info = None
        info = None
        try:
            # self.login()
            self.page_refresh()
            self.click(*el_business_manager.business_account_info)
            self.sleep(2)
            self.send_keys(*el_business_manager.opentime, '2019年07月', 3)  # 启用期间
            self.click(*el_business_manager.cost_check)  # 成本核算
            self.click(*el_business_manager.account_info_save)

            check_info = self.check_data(el_business_manager.account_save_tips, business_data.account_save_tips)

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def tear_down(self):
        try:
            self.load_url(login_data.login_url)
            self.page_refresh()
            self.click(*el_home_page.customer_manager_page)
            self.click(*el_business_manager.normal_filter)
            self.click(*el_business_manager.select_all_business)
            self.sleep(1)
            self.click(*el_business_manager.batch_delete_btn)
            self.sleep(2)
            self.clear(*el_business_manager.ipt_delete_pwd)
            self.send_keys(*el_business_manager.ipt_delete_pwd, login_data.password)
            self.click(*el_business_manager.delete_confirm)
            self.sleep(2)
            self.click(*el_business_manager.s_delete_btn)
        except Exception as why:
            print('没有要删除的企业')
        finally:
            print('测试重置完毕')
            assert True
