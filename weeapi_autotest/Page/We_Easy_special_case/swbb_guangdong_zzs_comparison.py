# !@coding  :utf-8 
# !@Time    :2021/1/12 13:51
# !@Author  :liulei
from Page.BasePage import BasePage
from element.WeEasy import el_business_manager
from element.WeEasy import el_home_page
from element.WeEasy.el_account_set import statement_swbb, account_home
from element.WeEasy.el_rwbb_comparison import el_guangdong_zzs_bb
from element.WeEasy.el_shuiju import el_guangdong


class SwbbComparison(BasePage):

    def zzs_comparison(self):
        case_name = '广东增值税报表比对'
        print(case_name, "|开始执行")

        check_info = self.comparison()

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def comparison(self):
        shuiju_info = self.collect_shuiju_zzsbb()
        we_info = self.collect_we_zzsbb()
        check_info = None

        shuiju_list = []
        for i in shuiju_info:
            print(i)
            try:
                info = i.replace(',', '')
            except AttributeError:
                info = ''
            if i == '0.00':
                info = ''
            print(info)
            shuiju_list.append(info)
        print(we_info)
        print('==================')
        print(shuiju_list)

        if shuiju_list == we_info:
            check_info = True
        for i, j in zip(shuiju_list, we_info):
            print(i, ':', j)
            print(i == j)
            print('================')
        print(len(we_info))
        print(len(shuiju_list))
        return check_info

    def collect_we_zzsbb(self):

        case_name = '唯易税务报表取样'
        print(case_name, "|开始执行")

        check_info = None
        info = None

        info_list = []
        self.login()
        self.enter_page()
        self.click(*statement_swbb.zzs_view)
        self.switch_to_window()

        for i in el_guangdong_zzs_bb.we_zzsbb:
            info = self.get_element_text('xpath', i, name='oldvalue')
            print(info)
            info_list.append(info)
        for a in info_list:
            if a is None:
                a = 'None'

        return info_list

    def collect_shuiju_zzsbb(self):
        case_name = '广东税务报表取样'
        print(case_name, "|开始执行")

        check_info = None
        info = None
        info_list = []
        try:
            self.login_guangdong()
            self.sleep(2)
            self.move(*el_guangdong.tax)
            self.click(*el_guangdong.tax_declaration)
            self.click(*el_guangdong.declare_correct)
            self.switch_to_frame(*el_guangdong.change_iframe)
            self.click(*el_guangdong.declare_types)
            self.click(*el_guangdong.added_value_tax)
            self.clear(*el_guangdong.declare_start_date)
            self.clear(*el_guangdong.declare_end_date)
            self.send_keys(*el_guangdong.belongs_start_date, '2020-12-01')
            self.send_keys(*el_guangdong.belongs_end_date, '2020-12-31')
            self.click(*el_guangdong.search_btn)

            self.click(*el_guangdong.correct_declare)
            self.switch_to_window()
            self.page_refresh()
            self.sleep(2)
            self.switch_to_default_frame()
            self.click(*el_guangdong.close_tips_btn0)
            self.sleep(10)

            self.switch_to_frame(*el_guangdong.change_iframe2)
            self.click(*el_guangdong.close_tips_btn1)
            self.sleep(1)
            self.click(*el_guangdong.close_tips_btn3)
            self.sleep(1)
            self.click(*el_guangdong.close_tips_btn4)

            self.switch_to_frame(*el_guangdong.change_iframe1)
            for i in el_guangdong_zzs_bb.shuiju_zzsbb:
                info = self.js_script(i)
                print(info)
                info_list.append(info)
        except Exception as why:
            print(why)

        return info_list

    def enter_page(self):
        self.page_refresh()
        self.click(*el_home_page.customer_manager_page)
        self.click(*el_business_manager.enter_btn2)
        self.sleep(2)
        self.page_refresh()
        self.move(*account_home.bb)
        self.click(*statement_swbb.swbb)
        self.switch_to_frame(*statement_swbb.change_iframe)
