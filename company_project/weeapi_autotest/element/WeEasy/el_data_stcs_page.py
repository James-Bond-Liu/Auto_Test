# !@coding  :utf-8
# !@Time    :2021/2/7 16:00
# !@Author  :liulei

"""
数据统计
"""
# 客户统计
client_btn = ('xpath', '//*[@name="menu-24501"]')
client_check_page = ('xpath', '//span[text()="客户统计"]')
# 工作明细
work_btn = ('xpath', '//*[@name="menu-24502"]')
work_detail_check_page = ('xpath', "//li[text()='工作明细']")
# 客户数据
client_data_btn = ('xpath', '//*[@name="menu-24503"]')
client_data_check_page = ('xpath', "//li[text()='客户数据']")
page_list = [client_btn, work_btn, client_data_btn]
check_list = [client_check_page, work_detail_check_page, client_data_check_page]
