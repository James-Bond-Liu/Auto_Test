# !@coding  :utf-8 
# !@Time    :2021/1/7 15:45
# !@Author  :liulei

tags = ('xpath', '//*[@link="/company/default_tags"]')
delete_check = ('xpath', '//*[text()="标签3"]')
select_box = ('xpath', '//*[@data-reactid=".0.1.1.1"]//tr[3]//*[@type="checkbox"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/default_tags"]')

add_tags = ('xpath', '//*[@name="btn-24205001"]')
ipt_tags_name = ('id', 'bqmc')
add_tags_confirm = ('xpath', '//*[@class="modal fade in"]//*[@onclick="addOrUpdate()"]')
tags_name = '//tbody[@data-reactid=".0.1.1.1"]//tr[%s]//td[2]'

delete_tags = ('xpath', '//*[@name="btn-24205002"]')
delete_confirm = ('xpath', '//*[@data-reactid=".1.0.2.0"]')
