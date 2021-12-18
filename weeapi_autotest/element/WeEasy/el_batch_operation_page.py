# !@coding  :utf-8 
# !@Time    :2021/2/7 16:06
# !@Author  :liulei

"""
批量操作
"""

batch_collect_btn = ('xpath', '//*[@name="menu-22201"]')
batch_settle_btn = ('xpath', '//*[@name="menu-22202"]')
batch_setting_btn = ('xpath', '//*[@name="menu-22203"]')
batch_copy_btn = ('xpath', '//*[@name="menu-22205"]')
# batch_bank_btn = ('xpath', '//a[text()="批量银行采集"]')
batch_back_btn = ('xpath', '//a[text()="批量备份"]')
batch_list = [batch_collect_btn, batch_settle_btn, batch_setting_btn, batch_copy_btn, batch_back_btn]

batch_collect_check_page = ('xpath', '//li[text()="批量采集"]')
batch_settle_check_page = ('xpath', '//li[text()="批量结账"]')
batch_setting_check_page = ('xpath', '//li[text()="批量设置"]')
batch_copy_check_page = ('xpath', '//li[text()="批量复制上期"]')
# batch_bank_check_page = ('xpath', '//li[text()="批量银行采集"]')
batch_back_check_page = ('xpath', '//li[text()="批量备份"]')
check_list = [batch_collect_check_page, batch_settle_check_page, batch_setting_check_page, batch_copy_check_page,
              batch_back_check_page]
