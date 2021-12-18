# !@coding  :utf-8 
# !@Time    :2021/2/7 16:06
# !@Author  :liulei

from Page.BasePage import BasePage
from element.WeEasy import el_home_page as home
from element.WeEasy import el_cszb_page as element
from data.config import cszb_data


class Cszb(BasePage):

    def cszb_page_check(self):
        case_name = "财税指标界面检查"
        print(case_name, "|开始执行")

        check_info = None

        try:
            self.click(*home.cszb)
            check_info = self.check_data(element.cszb_check_page, cszb_data.cszb_check_page)

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
