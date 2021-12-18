# !@coding  :utf-8 
# !@Time    :2021/1/7 19:48
# !@Author  :liulei

from Page.BasePage import BasePage
from data.config import account_set_setting_data
from element.WeEasy.el_account_set import process_expense_invoice, account_home


class Xxfp(BasePage):
    """
    账套-设置-销项发票中的功能
    """
    
    filter_list = []
    
    def import_xxfp(self):
        case_name = '导入销项发票'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            
            self.enter_page_too(account_home.ywcl, process_expense_invoice.xxfp, process_expense_invoice.change_iframe)
            self.import_flow(account_set_setting_data.xxfp_data)
            self.import_flow(account_set_setting_data.xxfp_s_data)
            
            self.sleep(3)
            check_info = self.check_data(process_expense_invoice.check_page, account_set_setting_data.xxfp_import_check)
        
        except Exception as why:
            print('why', why)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    @BasePage._base
    def auto_create_inventory(self):
        case_name = '销项发票自动创建存货'
        print(case_name, "|开始执行")
        # self.login()
        self.enter_page_too(account_home.ywcl, process_expense_invoice.xxfp, process_expense_invoice.change_iframe)
        self.clicks(process_expense_invoice.auto_create_inventory_element)
        self.select_value(*process_expense_invoice.create_filter, value='100')
        self.sleep(2)

        for i in range(1, 4):
            self.send_keys('xpath', process_expense_invoice.ipt_inventory_unit % i, '个')
        for i in range(4, 25):
            info = self.get_element_text('xpath', process_expense_invoice.select_inventory_type % i, open=True)
            if '请选择存货类别' in info:
                self.click('xpath', process_expense_invoice.ipt_inventory_type % i, open=2)
                self.click('xpath', process_expense_invoice.inventory_type_item % i, open=2)
                
            else:
                pass
        
        for i in range(1, 25):
            self.click('xpath', process_expense_invoice.add_inventory_type % i)
            check = self.get_element_text('xpath', process_expense_invoice.add_inventory_type % i, open=False)
            n = 0
            while check != '已新增存货':
                check = self.get_element_text('xpath', process_expense_invoice.add_inventory_type % i, open=False)
                self.click('xpath', process_expense_invoice.add_inventory_type % i)
                n += 1
                if n > 10:
                    break
        self.clicks(process_expense_invoice.create_btn)
        self.clicks(process_expense_invoice.batch_settlement_confirm)
        check_info = self.check_data(process_expense_invoice.create_success, account_set_setting_data.xxfp_auto_create)
        
        return case_name, check_info
    
    def check_invoice_data(self):
        case_name = '检查销项发票数据'
        print(case_name, "|开始执行")
        
        check_info = None
        info_list1 = []
        info_list2 = []
        try:
            self.click(*process_expense_invoice.refresh_btn)
            self.click(*process_expense_invoice.invoice_click)
            self.click(*process_expense_invoice.invoice_show_all)
            first = self.get_element_text(*process_expense_invoice.first_row_invoice_data)
            info_list1.append(first)
            for i in range(2, 6):
                info = self.get_element_text('xpath', process_expense_invoice.first_invoice_data % i)
                info_list1.append(info)
            info_list1.append((self.get_element_text(*process_expense_invoice.tax_total_price)))
            info_list1.append((self.get_element_text(*process_expense_invoice.tax_amount)))
            for i in range(1, 6):
                info = self.get_element_text('xpath', process_expense_invoice.invoice_money % i, name='value')
                info_list2.append(info)
            info_list2.append((self.get_element_text(*process_expense_invoice.invoice_total, name='value')))
            info_list2.append((self.get_element_text(*process_expense_invoice.invoice_total_price, name='value')))
            
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
        case_name = '销项发票查看汇总'
        print(case_name, "|开始执行")
        
        check_info = None
        info_list1 = []
        info_list2 = []
        invoice_info = 0.00
        invoice_info1 = 0.00
        invoice_info2 = 0.00
        try:
            self.click(*process_expense_invoice.refresh_btn)
            self.click(*process_expense_invoice.view_amount)
            for i in range(4, 7):
                info = self.get_element_text('xpath', process_expense_invoice.amount % i)
                info1 = (info.split('：')[-1])
                info2 = info1.replace(',', '')
                info_list1.append(info2)
            for i in range(2, 8, 2):
                info = self.get_element_text('xpath', process_expense_invoice.invoice_amount % i)
                info_ed = float(info.replace(',', ''))
                invoice_info += info_ed
                
                info1 = self.get_element_text('xpath', process_expense_invoice.invoice_total_amount % i)
                info1_ed = float(info1.replace(',', ''))
                invoice_info1 += info1_ed
                
                info2 = self.get_element_text('xpath', process_expense_invoice.invoice_price_amount % i)
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
        case_name = '销项发票结算'
        print(case_name, "|开始执行")

        check_info = None
        try:
            filter_info = self.filter_check(process_expense_invoice.settlement_filter, 1)
            self.filter_list.append(filter_info)
            self.click(*process_expense_invoice.refresh_btn)
            self.click(*process_expense_invoice.invoice_click)
            self.click(*process_expense_invoice.settlement)
            self.click(*process_expense_invoice.settlement_btn)
            check_info = self.check_data(process_expense_invoice.settlement_info, '交易(结算登记)')
            
            filter_info = self.filter_check(process_expense_invoice.settlement_filter, 2)
            self.filter_list.append(filter_info)
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def batch_settlement_invoice(self):
        case_name = '销项发票批量结算'
        print(case_name, "|开始执行")
        
        check_info = None
        try:
            
            self.click(*process_expense_invoice.refresh_btn)
            self.sleep(1)
            self.click(*process_expense_invoice.select_all)
            self.click(*process_expense_invoice.more_func)
            self.click(*process_expense_invoice.batch_settlement_btn)
            self.click(*process_expense_invoice.batch_set_btn)
            self.click(*process_expense_invoice.batch_settlement_confirm)
            
            check_info = self.check_data(process_expense_invoice.batch_set_info, '批量结算成功。')
        
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
            
            filter_info = self.filter_check(process_expense_invoice.unsettlement_filter, 1)
            self.filter_list.append(filter_info)
            self.click(*process_expense_invoice.invoice_click)
            self.click(*process_expense_invoice.delete_settlement)
            self.click(*process_expense_invoice.delete_settlement_confirm)
            check_info = self.check_data(process_expense_invoice.settlement_info, None)
            
            filter_info = self.filter_check(process_expense_invoice.unsettlement_filter, 2)
            self.filter_list.append(filter_info)
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def create_vouch(self):
        case_name = '销项发票生成凭证'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            filter_info = self.filter_check(process_expense_invoice.vouch_filter, 1)
            self.filter_list.append(filter_info)
            self.click(*process_expense_invoice.refresh_btn)
            self.click(*process_expense_invoice.select_all)
            self.sleep(2)
            self.click(*process_expense_invoice.create_vouch)
            self.click(*process_expense_invoice.create_vouch_confirm)
            
            check_info = self.check_data(process_expense_invoice.check_vouch_num, None, 2)
            filter_info = self.filter_check(process_expense_invoice.vouch_filter, 2)
            self.filter_list.append(filter_info)
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def delete_vouch(self):
        case_name = '销项发票删除凭证'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            filter_info = self.filter_check(process_expense_invoice.unvouch_filter, 1)
            self.filter_list.append(filter_info)
            self.click(*process_expense_invoice.refresh_btn)
            self.click(*process_expense_invoice.select_all)
            self.sleep(2)
            self.click(*process_expense_invoice.more_func)
            self.click(*process_expense_invoice.delete_vouch)
            self.click(*process_expense_invoice.delete_vouch_confirm)
            
            check_info = self.check_data(process_expense_invoice.check_vouch_num, None)
            filter_info = self.filter_check(process_expense_invoice.unvouch_filter, 2)
            self.filter_list.append(filter_info)
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def add_invoice(self):
        case_name = '新增一个发票'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_expense_invoice.refresh_btn)
            for i in account_set_setting_data.xxfp_add_invoice_type:
                self.add_invoice_flow(i)
            
            check_info = self.check_data(process_expense_invoice.check_page, account_set_setting_data.xxfp_add_check)
        
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    def clear_xxfp(self):
        case_name = '清空销项发票设置'
        print(case_name, "|开始执行")
        
        info = None
        check_info = None
        
        try:
            self.click(*process_expense_invoice.refresh_btn)
            self.click(*process_expense_invoice.select_all)
            self.click(*process_expense_invoice.more_func)
            self.click(*process_expense_invoice.more_delete)
            self.click(*process_expense_invoice.delete_confirm)
            
            check_info = self.check_data(process_expense_invoice.check_page, '共[0]条')
        
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
    
    def import_flow(self, data_target):
        self.click(*process_expense_invoice.ipt_xxfp)
        self.send_keys(*process_expense_invoice.upload, data_target)
        self.sleep(2)
        self.click(*process_expense_invoice.next_step)
        self.click(*process_expense_invoice.confirm)
    
    def add_invoice_flow(self, invoice):
        self.move(*process_expense_invoice.add_invoice)
        self.sleep(0.5)
        self.click(*process_expense_invoice.add_btn)
        self.sleep(1)
        self.select_value(*process_expense_invoice.ipt_invoice_type, invoice)
        self.click(*process_expense_invoice.ipt_costomer)
        self.click(*process_expense_invoice.costomer_select)
        self.click(*process_expense_invoice.select_costomer)
        self.click(*process_expense_invoice.ipt_type)
        self.click(*process_expense_invoice.select_item)
        self.click(*process_expense_invoice.item_show_all)
        self.click(*process_expense_invoice.select_type)
        
        self.select_value(*process_expense_invoice.select_item1, value='2')
        # self.click(*process_expense_invoice.add_invoice_save_btn)
        self.sleep(1)
        self.send_keys(*process_expense_invoice.ipt_amount, '13')
        self.click(*process_expense_invoice.ipt_transaction)
        self.click(*process_expense_invoice.select_transaction)
        
        self.click(*process_expense_invoice.add_invoice_save_btn)
        self.sleep(3)
    
    def filter_check(self, filter_type, search_type):
        self.click(*process_expense_invoice.refresh_btn)
        self.click(*process_expense_invoice.show_search)
        self.click(*filter_type)
        filter_check = self.check_data(process_expense_invoice.check_row, None, search_type)
        self.click(*process_expense_invoice.refresh_btn)
        self.sleep(2)
        return filter_check
