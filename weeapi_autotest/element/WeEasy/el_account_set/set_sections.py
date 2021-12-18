# !@coding  :utf-8 
# !@Time    :2021/1/7 14:36
# !@Author  :liulei

# !@coding  :utf-8
# !@Time    :2021/1/7 14:11
# !@Author  :liulei

sections = ('xpath', '//*[@link="/company/sections"]')
delete_check = ('xpath', '//*[text()="项目3"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/sections"]')

add_sections = ('xpath', '//*[@name="btn-24204001"]')
ipt_sections_name = ('id', 'bmmc')
add_sections_confirm = ('xpath', '//*[@class="actions top20px bottom10px "]//*[@onclick="taxSave()"]')
sections_name = '//tbody//tr[%s]//td[@class="section-child"]'

delete_sections = ('xpath', '//tbody//tr[3]//td[8]//a//i')
