# !@coding  :utf-8 
# !@Time    :2021/2/7 19:51
# !@Author  :liulei

"""
设置界面
"""

section_manager_check_page = ('xpath', '//li[text()="部门管理"]')
section_manager_btn = ('xpath', '//*[@name="menu-22301"]')

role_manager_check_page = ('xpath', '//li[text()="角色管理"]')
role_manager_btn = ('xpath', '//*[@name="menu-22302"]')

authorization_check_page = ('xpath', '//li[text()="授权情况"]')
authorization_btn = ('xpath', '//*[@name="menu-22303"]')

page_list = [section_manager_btn, role_manager_btn, authorization_btn]
check_list = [section_manager_check_page, role_manager_check_page, authorization_check_page]
