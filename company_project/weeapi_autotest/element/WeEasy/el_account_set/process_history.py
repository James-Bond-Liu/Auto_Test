# !@coding  :utf-8 
# !@Time    :2021/1/8 9:40
# !@Author  :liulei

history = ('xpath', '//*[@link="/lspz/index"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/lspz/index"]')

history_import = ('xpath', '//*[@data-reactid=".0.1.0.0.1"]')

check_data = ('xpath', '//*[@data-reactid=".0.1.0.0.4.0"]')

delete_history = ('xpath', '//*[@class="bulk-destroy btn btn-small btn-danger"]')
delete_confirm = ('id', 'confirmButton')

select_box = ('xpath', '//*[@data-reactid=".0.1.1.0.0.0.0"]')

check_import_status = ('xpath', '//*[@class="notification-message"][contains(.,("导入成功"))]')
