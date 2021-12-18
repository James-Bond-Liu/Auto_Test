# !@coding  :utf-8 
# !@Time    :2021/1/8 14:27
# !@Author  :liulei

subject = ('xpath', '//*[@link="/company/account_items"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/account_items"]')

add_subject = ('xpath', '//*[@name="btn-24206002"]')
ipt_subject_name = ('id', 'new_kmmc')
add_subject_confirm = ('xpath', '//*[text()="保存"]')
add_confirm = ('xpath', '//*[@class="modal fade in"]//*[@value="确认"]')
check_sjt1 = ('xpath', '//*[text()="科目1"]')
check_sjt2 = ('xpath', '//*[text()="科目2"]')
check_sjt3 = ('xpath', '//*[text()="科目3"]')

subject_edit = ('xpath', '//*[@class="account-item-tr clickable"][14]//*[@name="btn-24206003"]')
subject_delete = ('xpath', '//*[@name="btn-24206004"]')
subject_delete_confirm = ('xpath', '//*[@class="btn btn-large btn-danger"]')
