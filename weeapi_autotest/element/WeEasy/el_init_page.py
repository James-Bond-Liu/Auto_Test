# !@coding  :utf-8 
# !@Time    :2021/2/7 16:00
# !@Author  :liulei

"""
初始化
"""

# 财务初始化
finance_init_btn = ('xpath', '//*[@name="menu-21001"]')
finance_init_check_page = ('xpath', '//li[text()="财务初始化"]')

# 申报数据同步
declare_data_sync_btn = ('xpath', '//*[@name="menu-21002"]')
declare_data_sync_check_page = ('xpath', '//li[text()="申报数据同步"]')

page_list = [finance_init_btn, declare_data_sync_btn]
check_list = [finance_init_check_page, declare_data_sync_check_page]
