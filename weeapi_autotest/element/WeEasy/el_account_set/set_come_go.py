# !@coding  :utf-8 
# !@Time    :2021/1/7 14:11
# !@Author  :liulei

com_go = ('xpath', '//*[@link="/company/partners/else"]')
delete_check = ('xpath', '//*[text()="往来3"]')
select_box = ('xpath', '//*[text()="往来3" ]//preceding-sibling::td[2]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/partners/else"]')

add_com_go = ('xpath', '//*[@data-reactid=".0.1.0.0.0.1"]')
ipt_com_go_name = ('id', 'partner_name')
add_com_go_confirm = ('xpath', '//*[@class="modal fade in"]//*[@onclick="taxSave()"]')
com_go_name = '//tbody[1]//tr[%s]//td[3]'

delete_com_go = ('xpath', '//*[@name="btn-24202003"]')
delete_confirm = ('xpath', '//*[@data-reactid=".1.0.2.0"]')
