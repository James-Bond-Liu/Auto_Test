# !@coding  :utf-8 
# !@Time    :2021/1/7 19:48
# !@Author  :liulei

import pymysql

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from data.config import login_data
from element.WeEasy import el_business_manager, el_home_page
from element.WeEasy.el_account_set import process_income_invoice, account_home


class Jxfp(BasePage):
    """
    账套-设置-进项发票中的功能
    """

    filter_list = []

    def import_jxfp(self):
        case_name = '导入进项发票'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:

            self.enter_page_too(account_home.ywcl, process_income_invoice.jxfp, process_income_invoice.change_iframe)
            self.import_flow(account_set_setting_data.jxfp_data)
            info = self.get_element_text(*process_income_invoice.check_page)
            if info:
                check_info = True

        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def check_invoice_data(self):
        case_name = '检查进项发票数据'
        print(case_name, "|开始执行")

        check_info = None
        info_list1 = []
        info_list2 = []
        try:
            self.click(*process_income_invoice.refresh_btn)
            self.sleep(1)
            self.click(*process_income_invoice.invoice_click)
            self.click(*process_income_invoice.invoice_show_all)
            first = self.get_element_text(*process_income_invoice.first_row_invoice_data)
            info_list1.append(first)
            for i in range(2, 7):
                info = self.get_element_text('xpath', process_income_invoice.first_invoice_data % i)
                info_list1.append(info)
            info_list1.append((self.get_element_text(*process_income_invoice.tax_total_price)))
            info_list1.append((self.get_element_text(*process_income_invoice.tax_amount)))
            for i in range(0, 6):
                info = self.get_element_text('xpath', process_income_invoice.invoice_money % i, name='value')
                info_list2.append(info)
            info_list2 = info_list2[::-1]
            info_list2.append((self.get_element_text(*process_income_invoice.invoice_total, name='value')))
            info_list2.append((self.get_element_text(*process_income_invoice.invoice_total_price, name='value')))

            print(info_list1)
            print('=========')
            print(info_list2)
            if info_list1 == info_list2:
                check_info = True

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def check_invoice_amount(self):
        case_name = '进项发票查看汇总'
        print(case_name, "|开始执行")

        check_info = None
        info_list1 = []
        info_list2 = []
        invoice_info = 0.00
        invoice_info1 = 0.00
        invoice_info2 = 0.00
        try:
            self.click(*process_income_invoice.refresh_btn)
            self.sleep(1)
            self.click(*process_income_invoice.view_amount)
            for i in range(5, 8):
                info = self.get_element_text('xpath', process_income_invoice.amount % i)
                info1 = (info.split('：')[-1])
                info2 = info1.replace(',', '')
                info_list1.append(info2)
            for i in range(2, 10, 2):
                info = self.get_element_text('xpath', process_income_invoice.invoice_amount % i)
                info_ed = float(info.replace(',', ''))
                invoice_info += info_ed

                info1 = self.get_element_text('xpath', process_income_invoice.invoice_total_amount % i)
                info1_ed = float(info1.replace(',', ''))
                invoice_info1 += info1_ed

                info2 = self.get_element_text('xpath', process_income_invoice.invoice_price_amount % i)
                info2_ed = float(info2.replace(',', ''))
                invoice_info2 += info2_ed

            info_list2.append('%.2f' % invoice_info)
            info_list2.append('%.2f' % invoice_info1)
            info_list2.append('%.2f' % invoice_info2)

            print(info_list1)
            print('=========')
            print(info_list2)
            if info_list1 == info_list2:
                check_info = True

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def settlement_invoice(self):
        case_name = '进项发票结算'
        print(case_name, "|开始执行")

        check_info = None
        try:

            filter_info = self.filter_check(process_income_invoice.settlement_filter, 1)
            self.filter_list.append(filter_info)
            self.click(*process_income_invoice.invoice_click)
            self.click(*process_income_invoice.settlement)
            self.click(*process_income_invoice.settlement_btn)
            check_info = self.check_data(process_income_invoice.settlement_info, '交易(结算登记)')

            filter_info = self.filter_check(process_income_invoice.settlement_filter, 2)
            self.filter_list.append(filter_info)

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def batch_settlement_invoice(self):
        case_name = '进项发票批量结算'
        print(case_name, "|开始执行")

        check_info = None
        try:

            self.click(*process_income_invoice.refresh_btn)
            self.sleep(1)
            self.click(*process_income_invoice.select_all)
            self.click(*process_income_invoice.more_func)
            self.click(*process_income_invoice.batch_settlement_btn)
            self.click(*process_income_invoice.batch_set_btn)
            self.click(*process_income_invoice.batch_settlement_confirm)

            check_info = self.check_data(process_income_invoice.batch_set_info, '批量结算成功。')

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def delete_settlement_invoice(self):
        case_name = '删除结算'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:

            filter_info = self.filter_check(process_income_invoice.unsettlement_filter, 1)
            self.filter_list.append(filter_info)
            self.click(*process_income_invoice.invoice_click)
            self.click(*process_income_invoice.delete_settlement)
            self.click(*process_income_invoice.delete_settlement_confirm)
            check_info = self.check_data(process_income_invoice.settlement_info, None)

            filter_info = self.filter_check(process_income_invoice.unsettlement_filter, 2)
            self.filter_list.append(filter_info)
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def create_voucher(self):
        case_name = '生成凭证'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            filter_info = self.filter_check(process_income_invoice.vouch_filter, 1)
            self.filter_list.append(filter_info)
            self.click(*process_income_invoice.select_all)
            self.click(*process_income_invoice.create_pz)
            self.click(*process_income_invoice.create_pz_confirm)
            check_info = self.check_data(process_income_invoice.check_pzzh, None, 2)

            filter_info = self.filter_check(process_income_invoice.vouch_filter, 2)
            self.filter_list.append(filter_info)
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def delete_vouch(self):
        case_name = '进项发票删除凭证'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            filter_info = self.filter_check(process_income_invoice.unvouch_filter, 1)
            self.filter_list.append(filter_info)
            self.click(*process_income_invoice.select_all)
            self.sleep(2)
            self.click(*process_income_invoice.more_func)
            self.click(*process_income_invoice.delete_vouch)
            self.sleep(1)
            self.click(*process_income_invoice.delete_vouch_confirm)

            check_info = self.check_data(process_income_invoice.check_vouch_num, None)

            filter_info = self.filter_check(process_income_invoice.unvouch_filter, 2)
            self.filter_list.append(filter_info)

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def batch_edit(self):
        case_name = '批量编辑'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.click(*process_income_invoice.refresh_btn)
            self.sleep(5)
            self.click(*process_income_invoice.select_all)
            self.click(*process_income_invoice.batch_edit)
            self.click(*process_income_invoice.edit_settlement)
            self.click(*process_income_invoice.select_edit_settlement)
            self.click(*process_income_invoice.save_edit)
            self.click(*process_income_invoice.save_confirm)
            self.sleep(2)
            self.click(*process_income_invoice.invoice_click)

            check_info = self.check_data(('xpath', process_income_invoice.ipt_jysx % 5), source='原材料',
                                         name_type='value')

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def add_invoice(self):
        case_name = '新增发票'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.click(*process_income_invoice.refresh_btn)
            self.sleep(1)
            for i in account_set_setting_data.jxfp_add_invoice_type:
                self.add_invoice_flow(i)

            check_info = self.check_data(process_income_invoice.check_invoice_num,
                                         account_set_setting_data.jxfp_add_check)

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def clear_jxfp(self):
        case_name = '清空进项发票'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            self.enter_page_too(account_home.ywcl, process_income_invoice.jxfp, process_income_invoice.change_iframe)
            self.select_value(*process_income_invoice.page_filter, value='200')
            self.sleep(2)
            self.click(*process_income_invoice.select_all)
            self.click(*process_income_invoice.more_func)
            self.click(*process_income_invoice.more_delete)
            self.click(*process_income_invoice.delete_confirm)
            check_info = self.check_data(process_income_invoice.check_page, None)

            self.import_flow(account_set_setting_data.jxfp_data)

        except Exception as why:
            print('why', why)
        #
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def autocomple(self):
        case_name = '导入进项发票，自动补全'
        print(case_name, "|开始执行")

        info = None
        check_info = None

        try:
            # self.login()
            self.enter_page_too(account_home.ywcl, process_income_invoice.jxfp, process_income_invoice.change_iframe)
            self.import_flow(account_set_setting_data.jxfp_autocomple_data, 1)

            info = None
            n = 0
            while info == '共[0]条':
                self.sleep(60)
                self.click(*process_income_invoice.refresh_btn)
                info = self.get_element_text(*process_income_invoice.check_invoice_num)
                try:
                    info = info.replace(' ', '')
                    print(info)
                except ValueError:
                    print('格式错误')
                if n >= 5:
                    break
                n += 1
            self.click(*process_income_invoice.confirm)
            if self.sql_autocomple():
                check_info = True

            self.load_url(login_data.login_url)
            self.click(*el_home_page.customer_manager_page)
            self.click(*el_business_manager.business_name1_enter)

        except Exception as why:
            print('why', why)
        #
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    def invoice_filter(self):
        case_name = '发票得查询条件'
        print(case_name, "|开始执行")

        check_info = None

        try:
            print(self.filter_list)
            for i in range(0, len(self.filter_list)):
                if self.filter_list[i] is not True:
                    print('filter %s 查询失败' % i)
                    check_info = False
                    break
                else:
                    check_info = True
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'

    """
    模块方法
    """

    def import_flow(self, invoice, choose=None):
        self.click(*process_income_invoice.ipt_jxfp)
        self.sleep(2)
        self.send_keys(*process_income_invoice.upload, invoice)
        self.sleep(2)
        self.click(*process_income_invoice.next_step)
        if choose:
            self.click(*process_income_invoice.operation_tips)
        else:
            self.click(*process_income_invoice.tips)
            self.click(*process_income_invoice.confirm)

    def add_invoice_flow(self, invoice):
        self.move(*process_income_invoice.add_invoice)
        self.sleep(0.5)
        self.click(*process_income_invoice.add_btn)
        self.sleep(1)
        self.select_value(*process_income_invoice.ipt_invoice_type, invoice)
        self.click(*process_income_invoice.ipt_costomer)
        self.click(*process_income_invoice.select_costomer)
        self.click(*process_income_invoice.ipt_type)
        self.click(*process_income_invoice.select_item)

        if self.get_element_text(*process_income_invoice.select_type) == '购销合同':
            self.click(*process_income_invoice.select_type)
        else:
            self.click(*process_income_invoice.add_record)
            self.sleep(2)
            self.select_value(*process_income_invoice.tax_items, value='1124')
            self.select_value(*process_income_invoice.declare_form, value='QD_YHS_YFS_2019_1')
            self.click(*process_income_invoice.add_record_confirm)
            self.clear(*process_income_invoice.ipt_amount)
            self.click(*process_income_invoice.add_invoice_save_btn)

        self.click(*process_income_invoice.add_invoice_save_btn)
        # self.move(*process_income_invoice.ipt_amount)
        self.send_keys(*process_income_invoice.ipt_amount, '13')
        self.click(*process_income_invoice.ipt_transaction)
        self.click(*process_income_invoice.select_transaction)

        self.click(*process_income_invoice.add_invoice_save_btn)
        self.sleep(3)

    def filter_check(self, filter_type, search_type):
        self.click(*process_income_invoice.refresh_btn)
        self.sleep(1)
        self.click(*process_income_invoice.show_search)
        self.click(*filter_type)
        filter_check = self.check_data(process_income_invoice.check_page, None, search_type)
        self.click(*process_income_invoice.refresh_btn)
        self.sleep(2)
        return filter_check

    def sql_autocomple(self):
        # 进入该企业的编辑，获取需要的url
        self.load_url(login_data.login_url)
        self.click(*el_home_page.customer_manager_page)
        self.click(*el_business_manager.business_name1_edit)
        url_info = self.get_page_url()

        dispose_url = url_info.split('qynbm=')[1]
        url = dispose_url.split('&')[0]
        print('url:', url)
        check_info = None
        # 打开数据库连接
        # db = pymysql.connect(host="192.168.1.200", port=3306, user="root", password="TaxPlus@112233", db="taxplus_test",
        #                      charset='utf8')
        db = pymysql.connect(host="www.mi-guo.xyz", port=10017, user="we_dzgs_query", password="Ve+-RDS1+2021+query", db="taxplus_dzgs_jiangsu10",
                              charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT WYCGBZ FROM `tp_sys_jkgl_log` WHERE QYNBM ='%s'" % url)
        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchall()
        print(data)
        for i in data:

            if i[0] == '1':
                print('i', i)
                check_info = True
            else:
                print('i', i)
                check_info = False
                break
        # 关闭数据库连接
        db.close()
        print(check_info)
        return check_info


if __name__ == '__main__':
    pass
