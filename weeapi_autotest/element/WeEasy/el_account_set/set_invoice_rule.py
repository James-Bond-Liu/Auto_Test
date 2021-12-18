# !@coding  :utf-8 
# !@Time    :2021/1/18 11:08
# !@Author  :liulei

invoice_rule = ('xpath', '//*[@link="/invoice_matchers"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/invoice_matchers"]')

invoice_type = ('id', 'invoice_entry_side_str')

create_new_rule = ('xpath', '//*[@href="#invoice_creator"]')
costomer_box = ('id', 'gxfmcBox')
ipt_costomer = ('id', 'gxfmc')

ipt_transaction = ('xpath', '//*[@class="fcb-container"]//*[@name="account_item"]')
select_income_transaction = ('xpath', '//*[@class="fcb-text"]//*[text()="库存商品"]')
select_expense_transaction = ('xpath', '//*[@class="fcb-text"]//*[text()="销售商品收入及提供劳务收入"]')

ipt_item = ('xpath', '//*[@id="create-zspm"]/div/span/input')
select_item_type = ('xpath', '//*[@code="valueAddedTax"]')
item_showall = ('xpath', '//*[@class="item-name"][2]')
select_item = ('xpath', '//*[text()="一般计税方法-13%税率的货物"]')
click_i = ('xpath', '//*[text()="历史"]')

create_btn = ('id', 'invoice_btn')
create_tips = ('xpath', '//*[text()="匹配规则创建成功"]')
