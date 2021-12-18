# !@coding  :utf-8 
# !@Time    :2021/1/29 13:57
# !@Author  :LiuLei
from Page.BasePage import BasePage
from element.WeEasy.el_account_set import process_inventory, account_home
from data.config import account_set_setting_data


class Inventory(BasePage):
    
    def add_inventory_type(self):
        case_name = '新增存货类别'
        print(case_name, "|开始执行")
        
        check_info = None
        try:
            self.enter_page_too(account_home.ywcl, process_inventory.inventory_page, process_inventory.change_iframe)
            for i in account_set_setting_data.inventory_type:
                self.click(*process_inventory.inventory_type)
                self.click(*process_inventory.add_inventory_type)
                self.send_keys(*process_inventory.ipt_type_name, i)
                self.select_text(*process_inventory.select_type_sections, value='1405_库存商品')
                self.click(*process_inventory.save_inventory_type)
                self.sleep(2)
            self.get_screenshot_as_file()
            for i, k in zip(list(range(1, 4)), account_set_setting_data.inventory_type_check):
                for j, data in zip(list(range(3, 6)), k):
                    check_info = self.diff_data(process_inventory.add_type_check % (i, j), data)
                    if check_info is None:
                        check_info = False
                        break
                if check_info is False:
                    break
        except Exception as why:
            print('why', why)
        
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
    
    @BasePage._base
    def add_inventory(self):
        case_name = '新增存货'
        print(case_name, "|开始执行")
        self.click(*process_inventory.page_refresh)
        
        for i in account_set_setting_data.inventory_name:
            self.click(*process_inventory.add_inventory)
            self.send_keys(*process_inventory.inventory_name, i)
            self.send_keys(*process_inventory.inventory_unit, account_set_setting_data.inventory_unit)
            self.click(*process_inventory.save_add_inventory)
            self.sleep(2)
        check_info = self.check_data(process_inventory.inventory_count, account_set_setting_data.inventory_count)
        
        return case_name, check_info
    
    @BasePage._base
    def delete_inventory(self):
        case_name = '删除存货'
        print(case_name, "|开始执行")
        
        elements = [process_inventory.select_inventory, process_inventory.delete_inventory,
                    process_inventory.delete_confirm]
        
        self.click(*process_inventory.page_refresh)
        self.sleep(1)
        self.select_value(*process_inventory.inventory_filter, value='50')
        self.sleep(1)
        self.clicks(elements)
        check_info = self.check_data(process_inventory.inventory_count, account_set_setting_data.delete_inventory_count)
        return case_name, check_info
    
    @BasePage._base
    def add_bom(self):
        case_name = '新增bom表'
        print(case_name, "|开始执行")
        ts = [process_inventory.page_refresh, process_inventory.inventory_bom]
        check_list = []
        check_info = False
        
        self.enter_page_too(account_home.ywcl, process_inventory.inventory_page, process_inventory.change_iframe)
        self.clicks(ts)
        self.sleep(2)
        self.add_bom_flow(process_inventory.bom_elements)
        self.add_bom_flow(process_inventory.bom_elements[:-1] + [process_inventory.select_bom_product2])
        for i in range(1, 3):
            view = []
            for j in range(3, 6):
                info = self.get_element_text('xpath', process_inventory.check_item % (i, j))
                view.append(info)
            check_list.append(view)
        print('check_list', check_list)
        if check_list == account_set_setting_data.inventory_bom_check:
            check_info = True
        
        return case_name, check_info

    @BasePage._base
    def delete_bom(self):
        case_name = '删除bom表'
        print(case_name, "|开始执行")
        check_list = []
        check_info = False

        ts = [process_inventory.page_refresh, process_inventory.inventory_bom]
        self.clicks(ts)
        self.sleep(1)
        self.click('xpath', process_inventory.select_box % 2)
        
        self.click(*process_inventory.delete_inventory_bom)
        self.sleep(1)
        self.click(*process_inventory.delete_confirm)
        for i in range(3, 6):
            info = self.get_element_text('xpath', process_inventory.check_item % ('last()', i))
            check_list.append(info)
        if check_list == account_set_setting_data.inventory_bom_check[0]:
            check_info = True
    
        return case_name, check_info
    
    def add_bom_flow(self, element):
        self.clicks(element)
        for i in range(2, 7):
            self.click(*process_inventory.bom_add)
            try:
                self.click('xpath', process_inventory.bom_name % str(i-1))
                self.click('xpath', process_inventory.bom_item % i)
            except Exception as why:
                self.click('xpath', process_inventory.bom_name % str(i-1))
                self.click('xpath', process_inventory.bom_item % i)
            self.send_keys('xpath', process_inventory.bom_num % str(i-1), 1)
        self.click(*process_inventory.save_bom)
