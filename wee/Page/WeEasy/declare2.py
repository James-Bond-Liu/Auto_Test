# !@coding  :utf-8 
# !@Time    :2021/2/7 16:00
# !@Author  :liulei

from Page.BasePage import BasePage
from element.WeEasy import el_home_page as home
from element.WeEasy import el_declare2_page as element
from data.config import declare2_data as data


class Declare2(BasePage):

    def Declare2_page_check(self):
        case_name = "批量申报2.0界面检查"
        print(case_name, "|开始执行")

        check_info = None

        try:
            check = self.check_page(home.declare2, element.page_list,
                                    element.check_list, data.check_page_list)
            if len(check) != 0:
                check_info = False
            else:
                check_info =True
        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
