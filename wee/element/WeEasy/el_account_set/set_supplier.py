# !@coding  :utf-8 
# !@Time    :2021/1/7 11:37
# !@Author  :liulei

supplier = ('xpath', '//*[@link="/company/partners/supplier"]')
add_supplier = ('xpath', '//*[@data-reactid=".0.1.0.0.0.1"]')
ipt_supplier_name = ('id', 'partner_name')
add_supplier_confirm = ('xpath', '//*[@class="modal fade in"]//*[@onclick="taxSave()"]')
supplier_name = '//tbody[1]//tr[%s]//td[3]'
select_box = ('xpath', '//*[text()="天猫" ]//preceding-sibling::td[2]')
delete_supplier = ('xpath', '//*[@name="btn-24202003"]')
delete_confirm = ('xpath', '//*[@data-reactid=".1.0.2.0"]')
delete_check = ('xpath', '//*[text()="天猫"]')

change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/partners/supplier"]')
