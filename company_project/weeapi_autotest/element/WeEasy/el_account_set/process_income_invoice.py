# !@coding  :utf-8 
# !@Time    :2021/1/8 10:20
# !@Author  :liulei

jxfp = ('xpath', '//*[@link="/invoices?jxxbz=1"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/invoices?jxxbz=1"]')

"""导入"""
ipt_jxfp = ('xpath', '//*[@name="btn-23102002"]')
upload = ('xpath', '//*[@class="input-file-ch-sa"]')
next_step = ('xpath', '//*[@onclick="handleSubmit()"]')
tips = ('xpath', '//*[text()="ok"]')
confirm = ('xpath', '//*[@class="btn btn-default"][text()="确定"]')
operation_tips = ('xpath', '//*[@onclick="yes()"]')
check_page = ('xpath', '//tbody[1]//tr[1]//td[6][@class="xfmc-cell"]')
check_invoice_num = ('xpath', '//*[@id="pager"]/div/span/label')

select_all = ('id', 'selectAll')
more_func = ('xpath', '//*[text()="更多功能"]')
more_delete = ('id', 'more-delete')
delete_confirm = ('xpath', '//*[@class="bulk-destroyer-confirm btn btn-large btn-danger"]')

page_filter = ('xpath', '//*[@class="limit-select"]')

"""新增"""

add_invoice = ('id', 'deals-menubar-submenu-button')
add_btn = ('id', 'more-xz')

ipt_invoice_type = ('xpath', '//*[@class="taxes-select input-mini"]')
ipt_costomer = ('xpath', '//*[@class="khgysbox"]')
select_costomer = ('xpath', '//*[text()="武汉市聚荣璟大药房有限公司艺境店【客户】"]')

ipt_type = ('xpath', '//*[@class="zspmbox"]')
select_item = ('xpath', '//*[@data-code="stampTax"]//*[text()="印花税"]')
select_type = ('xpath', '//*[@class="item-name"]//*[text()="购销合同"]')
add_record = ('xpath', '//*[@class="col-zspm"]//*[@class="item-name"]')
tax_items = ('id', 'zspmdm_ds')
declare_form = ('id', 'dzbdbm_ds')
add_record_confirm = ('id', 'szjd-qy-btn_ds')

ipt_transaction = ('xpath', '//*[@class="ReactModalPortal"]//*[@name="account_item"]//parent::div')
select_transaction = ('xpath', '//*[@class="fcb-text"]//*[text()="库存商品"]')
ipt_amount = ('xpath', '//*[@name="amount"]')
add_invoice_save_btn = ('xpath', '//*[@class="header-buttons"]//button[1]')



"""发票"""
invoice_click = ('xpath', '//*[@id="list"]/table/tbody/tr[1]/td[6]')
invoice_show_all = ('xpath', '//*[@id="list"]/table/tbody/tr[2]/td[3]')
ipt_jysx = '//tr[last()-%s]//*[@name="account_item"]'
select_jysx = ('xpath', '//*[@class="menu-title"][text()="库存商品"]')
save_fp = ('xpath', '//*[@class="btn btn-primary xgjy"]')
select_fp = ('xpath', '//tr[1]//*[@class="checkbox"]')

invoice_money = '//tr[last()-%s]//*[@name="amount"]'  # 发票详细的交易事项金额
invoice_total = ('xpath', '//*[@name="total_amount"]')
invoice_total_price = ('xpath', '//*[@name="total_vat"]')
invoice_amount = '//*[@id="list"]/table/tbody/tr[%s]/td[5]'  # 每张发票得金额
invoice_total_amount = '//*[@id="list"]/table/tbody/tr[%s]/td[7]'  # 每张发票税额
invoice_price_amount = '//*[@id="list"]/table/tbody/tr[%s]/td[8]'  # 每张发票的价税合计

total_amount = ('xpath', '//*[@id="list"]/table/tbody/tr[7]/td[5]')  # 金额合计
tax_amount = ('xpath', '//*[@id="list"]/table/tbody/tr[7]/td[7]')  # 税额合计
tax_total_price = ('xpath', '//*[@id="list"]/table/tbody/tr[7]/td[8]')  # 价税合计

first_row_invoice_data = ('xpath', '//*[@id="list"]/table/tbody/tr[1]/td[12]')  # 第一张发票第一行的金额
first_invoice_data = '//*[@id="list"]/table/tbody/tr[%s]/td[4]'  # 第一张发票的其他行
"""凭证"""
create_pz = ('xpath', '//*[@name="btn-23102004"]')
create_pz_confirm = ('id', 'btn-register')
check_pz = ('xpath', '//*[@class="reconciled"]')
check_pzzh = ('xpath', '//tbody[1]//tr[1]//td[@class="pzzh-cell"]//a')
check_vouch_num = ('xpath', '//*[@id="list"]/table/tbody/tr[1]/td[9]/a')  # 检查凭证字号
delete_vouch = ('id', 'more-scpz')  # 删除凭证
delete_vouch_confirm = ('id', 'btn-quxiaodengji')

"""采集"""
collect = ('xpath', '//*[@name="btn-23102018"]')
collect_confirm = ('xpath', '//*[@class="caiji-confirm btn btn-large btn-primary"]')
check_jxfp_collect = ('xpath', '//div[@id="pager"]/div/span/label')
# check_jxfp_collect = ('xpath', '//*[text()="共  [ 3 ]  条"]')
refresh_btn = ('xpath', '//*[@onclick="javascript:refreshPage()"]')

"""结算"""
settlement = ('xpath', '//*[@id="list"]/table/tbody/tr[3]/td/div/div[4]/div/div[2]/div/table/tfoot/tr/td/button/span')
settlement_btn = ('xpath', '//*[@class="ReactModalPortal"]//*[text()="结算"]')
settlement_info = ('xpath', '//*[@id="list"]/table/tbody/tr[3]/td/div/div[4]/div/div[2]/div/table/tbody/tr/td[1]')
delete_settlement = ('xpath', '//*[@class="btn btn-danger js-remove"]')  # 删除结算按钮
delete_settlement_confirm = ('xpath', '//*[@class="btn btn-large btn-danger"]')
batch_settlement_btn = ('id', 'more-pljs')
batch_set_btn = ('xpath', '//*[@class="bulk-make-settlement-confirm btn btn-primary"]')
batch_settlement_confirm = ('xpath', '//*[@class="btn btn-primary confirm-done"]')
batch_set_info = ('xpath', '//*[text()="批量结算成功。"]')
"""查看汇总"""
view_amount = ('xpath', '//*[@name="btn-23102005"]')  # 查看汇总
amount = '//*[@id="dataTable"]/tbody/tr[1]/td[%s]'  # 查看汇总信息(5,6,7)

"""批量编辑"""
batch_edit = ('id', 'more-plbj')
edit_settlement = ('xpath', '//*[@id="bulk-editor"]/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/input')
select_edit_settlement = ('xpath', '//*[@class="fcb-text"]//*[text()="原材料"]')

edit_costomer = ('xpath', '//*[@id="bulk-editor"]/div/div/div[2]/div/div[1]/div[1]/div/div/span/input')
select_edit_costomer_type =('xpath', '//*[@code="partner_customer"]')
select_edit_costomer =('xpath', '//*[@class="main-title"]//*[text()="武汉市聚荣璟大药房有限公司艺境店【客户】"]')

edit_stamp = ('xpath', '//*[@id="bulk-editor"]/div/div/div[2]/div/div[1]/div[4]/div/div/span/input')
select_stamp = ('xpath', '//*[@class="ac_over combobox-line"]//*[text()="购销合同"]')

edit_product = ('xpath', '//*[@placeholder="例）项目"]')
select_product = ('xpath', '//*[@class="item"]//li[2]')

edit_sections = ('xpath', '//*[@placeholder="例）部门"]')
select_sections = ('xpath', '//*[@class="section"]//li[2]')


save_edit = ('xpath', '//*[@class="bulk-editor-confirm btn btn-small btn-primary"]')
save_confirm = ('xpath', '//*[@class="btn btn-primary confirm-done"]')



"""筛选器"""
show_search = ('xpath', '//*[@id="select-filter"]/span')
all_register_filter = ('xpath', '//*[@id="filter-status"]//button[1]')
register_filter = ('xpath', '//*[@id="filter-status"]//button[2]')
unregister_filter = ('xpath', '//*[@id="filter-status"]//button[3]')

all_vouch_filter = ('xpath', '//*[@id="filter-pzzt"]//button[1]')
vouch_filter = ('xpath', '//*[@id="filter-pzzt"]//button[3]')
unvouch_filter = ('xpath', '//*[@id="filter-pzzt"]//button[2]')

all_settlement_filter = ('xpath', '//*[@id="filter-jsbz"]//button[1]')
settlement_filter = ('xpath', '//*[@id="filter-jsbz"]//button[2]')
unsettlement_filter = ('xpath', '//*[@id="filter-jsbz"]//button[4]')
