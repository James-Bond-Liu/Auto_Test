# !@coding  :utf-8 
# !@Time    :2021/1/5 19:45
# !@Author  :liulei
from Page.BasePage import BasePage
from data.config import login_data
from element.WeEasy import el_login


class Login(BasePage):
    """
    登录操作
    
    """
    def login_ts(self):
        case_name = '客户登录'
        print(case_name, "|开始执行")
        try:
            self.login()
            self.load_url(login_data.login_url)
        except Exception as why:
            print('why', why)

        check_info = self.check_data(el_login.usr_info, login_data.realname)
        print('check_info', check_info)
        result_status = check_info
        print('=======================================================================================================')
        assert result_status, '登录失败'
