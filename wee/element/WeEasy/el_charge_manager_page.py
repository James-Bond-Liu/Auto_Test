# !@coding  :utf-8 
# !@Time    :2021/2/7 16:07
# !@Author  :liulei

"""
收费管理
"""

charge_manager_btn = ('xpath', '//*[@name="menu-24301"]')
statistics_btn = ('xpath', '//*[@name="menu-24302"]')
page_list = [charge_manager_btn, statistics_btn]

charge_manager_check_page = ('xpath', '//li[text()="收费管理"]')
statistics_check_page = ('xpath', '//li[text()="收费统计分析"]')
check_list = [charge_manager_check_page, statistics_check_page]
