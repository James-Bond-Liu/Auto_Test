# !@coding  :utf-8 
# !@Time    :2021/2/7 16:00
# !@Author  :liulei

business_view_btn = ('xpath', '//a[@name="menu-20301"]')
business_view_check_page = ('xpath', '//li[text()="报表一览"]')

tax_declaration_btn = ('xpath', '//*[@name="menu-20302"]')
tax_declaration_check_page = ('xpath', '//li[text()="税款申报"]')

zero_declaration_btn = ('xpath', '//*[@name="menu-20303"]')
zero_declaration_check_page = ('xpath', '//li[text()="零申报"]')

pay_btn = ('xpath', '//*[@name="menu-20304"]')
pay_check_page = ('xpath', '//li[text()="缴款"]')

fail_declare_btn = ('xpath', '//*[@name="menu-20305"]')
fail_declare_check_page = ('xpath', '//li[text()="漏报检查"]')

task_manager_btn = ('xpath', '//a[@name="menu-20306"]')
task_manager_check_page = ('xpath', '//li[text()="任务管理"]')

setting_btn = ('xpath', '//*[@name="menu-20307"]')
setting_check_page = ('xpath', '//li[text()="设置"]')

page_list = [business_view_btn, tax_declaration_btn, zero_declaration_btn, pay_btn, fail_declare_btn, task_manager_btn,
             setting_btn]
check_list = [business_view_check_page, tax_declaration_check_page, zero_declaration_check_page, pay_check_page,
              fail_declare_check_page, task_manager_check_page, setting_check_page]
