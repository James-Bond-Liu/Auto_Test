# !@coding  :utf-8 
# !@Time    :2021/2/7 16:06
# !@Author  :liulei

from Page.BasePage import BasePage
from element.WeEasy import el_home_page, el_batch_operation_page
from data.config import batch_operation_data


class BatchOperation(BasePage):
    """
    批量操作界面
    """

    def operation_page_check(self):
        case_name = "批量操作界面检查"
        print(case_name, "|开始执行")

        check = []
        check_info = None

        try:
            check = self.check_page(el_home_page.batch_operation, el_batch_operation_page.batch_list,
                                    el_batch_operation_page.check_list, batch_operation_data.check_page_list)
            if len(check) != 0:
                check_info = False
            else:
                check_info = True

        except Exception as why:
            print('why', why)

        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, case_name + '失败'
