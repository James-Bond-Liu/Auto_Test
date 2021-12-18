# !@coding  :utf-8 
# !@Time    :2021/2/7 19:48
# !@Author  :liulei

"""
唯易客
"""

account_setting_check_page = ("xpath", '//li[text()="账号设置"]')
account_setting_btn = ("xpath", '//*[@name="menu-24401"]')
message_manager_check_page = ("xpath", '//li[text()="消息管理"]')
message_manager_btn = ("xpath", '//*[@name="menu-24402"]')

page_list = [account_setting_btn, message_manager_btn]
check_list = [account_setting_check_page, message_manager_check_page]
