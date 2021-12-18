# !@coding  :utf-8 
# !@Time    :2021/1/7 14:36
# !@Author  :liulei

# !@coding  :utf-8
# !@Time    :2021/1/7 14:11
# !@Author  :liulei

product = ('xpath', '//*[@link="/company/items"]')
delete_check = ('xpath', '//*[text()="项目3"]')
select_box = ('xpath', '//*[@data-reactid=".0.1.2.1"]//tr[3]//*[@type="checkbox"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/items"]')

add_product = ('xpath', '//*[@name="btn-24203001"]')
ipt_product_name = ('id', 'item_name')
add_product_confirm = ('xpath', '//*[@class="modal fade in"]//*[@onclick="submit()"]')
product_name = '//tbody[@data-reactid=".0.1.2.1"]//tr[%s]//td[2]'

delete_product = ('xpath', '//*[@name="btn-24203002"]')
delete_confirm = ('xpath', '//*[@data-reactid=".1.0.2.0"]')
