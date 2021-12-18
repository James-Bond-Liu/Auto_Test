# !@coding  :utf-8 
# !@Time    :2021/2/22 11:26
# !@Author  :LiuLei
import os

# 申报测试登录账户
declare_username = 'declare@we.com'
# declare_username = '1069243976@qq.com'
declare_password = 'welcome'
# 测试后台申报任务放开
# url = 'http://192.168.1.200'
url = 'http://update.mi-guo.xyz'

# 后台的账号
manager_user = 'admin'
# 后台的密码
manager_pwd = 'VeAAf'

open_declare_url = url + ':8787/webmanage/commonController/updatedzbddzbdgl2.htm'

manager_url = url + ':8787/webmanage/jsp/login/main.jsp'
data_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\编码对象\表单对应关系.xlsx'
