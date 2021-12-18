# !@coding  :utf-8 
# !@Time    :2021/1/7 10:33
# !@Author  :liulei

# 客户
costomer = ('xpath', '//*[@link="/company/partners/customer"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/partners/customer"]')

add_costomer = ('xpath', '//*[@data-reactid=".0.1.0.0.0.1"]')
ipt_costomer_name = ('id', 'partner_name')
add_costomer_confirm = ('xpath', '//*[@onclick="taxSave()"]')

delete_costomer = ('xpath', '//*[@name="btn-24202003"]')
delete_confirm = ('xpath', '//*[@data-reactid=".1.0.2.0"]')
delete_check = ('xpath', '//*[text()="Google"]')

costomer_name = '//tbody[1]//tr[%s]//td[3]'
select_box = ('xpath', '//*[text()="Google"]//preceding-sibling::td[2]')
