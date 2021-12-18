# !@coding  :utf-8 
# !@Time    :2021/1/8 10:20
# !@Author  :liulei

xxfp = ('xpath', '//*[@link="/invoices"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/invoices"]')

ipt_xxfp = ('xpath', '//*[@name="btn-23101002"]')
upload = ('xpath', '//*[@class="input-file-ch-sa"]')
next_step = ('xpath', '//*[@onclick="handleSubmit()"]')
check_page = ('xpath', '//*[@id="pager"]/div/span/label')
check_row = ('xpath', '//*[@id="list"]/table/tbody/tr[1]/td[6]')

confirm = ('xpath', '//*[@class="btn btn-default"][text()="确定"]')
add_invoice = ('id', 'deals-menubar-submenu-button')
add_btn = ('id', 'more-xz')
batch_edit = ('id', 'more-plbj')
auto_create = ('xpath', '//*[@class="create-inventory"]')
ipt_create = ('xpath', '//*[@id="bulk-editor"]//*[@class="zdcjch"]//input')
auto_create_tips = ('xpath', '//*[text()="根据商品大类自动创建"]')
save_edit = ('xpath', '//*[@class="bulk-editor-confirm btn btn-small btn-primary"]')  # 保存编辑
save_confirm = ('xpath', '//*[@class="btn btn-primary confirm-done"]')  # 确认保存编辑
last_subject = ('xpath', '//tbody[@id="spmcCjchBody"]//tr[last()]//td[1]')  # 最后一个科目的序号
subject_num = '//tbody[@id="spmcCjchBody"]//tr[%s]//td[3]/select'  # select_text = '1405_库存商品'
subject_save = ('xpath', '//*[@onclick="saveSpmcChlb()"]')  # 保存创建的商品科目
edit_confirm_page = ('xpath', '//*[contains(text(),"批量编辑确认")]')  # 确认编辑界面
edit_confirm = ('xpath', '//*[@class="btn btn-primary confirm-chcjDetail"]')  # 确认存货创建详情
select_inventory_type = '//tbody[@id="chcjxqDivBody"]//tr[%s]//td[3]'
ipt_inventory_type = '//tbody[@id="chcjxqDivBody"]//tr[%s]//td[3]/div/a/span'
inventory_type_item = '//tbody[@id="chcjxqDivBody"]//tr[%s]//td[3]/div//*[text()="存货类别1"]'
inventory_type = '//tbody[@id="chcjxqDivBody"]//tr[%s]//td[3]'
add_inventory_type = '//tbody[@id="chcjxqDivBody"]//tr[%s]//td[13]/button'
ipt_inventory_unit = '//tbody[@id="chcjxqDivBody"]//tr[%s]//td[5]/input'
create_filter = ('id', 'pageAllTotal')  # select_value = '100'  创建存货详情界面显示多少条
create_btn = ('xpath', '//*[@name="createChBtn"]')
create_success = ('xpath', '//*[text()="批量编辑成功"]')

ipt_invoice_type = ('xpath', '//*[@class="taxes-select input-mini"]')
ipt_costomer = ('xpath', '//*[@class="khgysbox"]')
costomer_select = ('xpath', '//*[@data-code="partner_customer"]')
select_costomer = ('xpath', '//*[text()="武汉市聚荣璟大药房有限公司艺境店【客户】"]')

ipt_type = ('xpath', '//*[@class="zspmbox"]')
select_item = ('xpath', '//*[@data-code="valueAddedTax"]//*[text()="增值税"]')
select_item1 = ('xpath', '//*[@name="tax_entry_method"]')

item_show_all = ('xpath', '//span[text()="显示全部"]')
select_type = ('xpath', '//*[@class="item-name"]//*[text()="一般计税方法-13%税率的货物"]')
# select_type = ('xpath', '//*[@class="item-name"]//*[text()="购销合同"]')
# add_record = ('xpath', '//*[@class="col-zspm"]//*[@class="item-name"]')
# tax_items = ('id', 'zspmdm_ds')
# declare_form = ('id', 'dzbdbm_ds')
# add_record_confirm = ('id', 'szjd-qy-btn_ds')

ipt_transaction = ('xpath', '//*[@class="ReactModalPortal"]//*[@name="account_item"]//parent::div')
select_transaction = ('xpath', '//*[text()="销售商品收入及提供劳务收入"]')
ipt_amount = ('xpath', '//*[@name="amount"]')
add_invoice_save_btn = ('xpath', '//*[@class="header-buttons"]//button[1]')

select_all = ('id', 'selectAll')
more_func = ('xpath', '//*[text()="更多功能"]')
more_delete = ('id', 'more-delete')
delete_confirm = ('xpath', '//*[@class="bulk-destroyer-confirm btn btn-large btn-danger"]')

ipt_jysx = '//tr[last()-%s]//*[@name="account_item"]'
select_jysx = ('xpath', '//*[@class="menu-title"][text()="主营业务收入"]')
save_invoice = ('xpath', '//*[@class="btn btn-primary xgjy"]')
select_invoice = ('xpath', '//tr[1]//*[@class="checkbox"]')
invoice_click = ('xpath', '//*[@id="list"]/table/tbody/tr[1]/td[6]')
invoice_show_all = ('xpath', '//*[@id="list"]/table/tbody/tr[2]/td[3]')

first_row_invoice_data = ('xpath', '//*[@id="list"]/table/tbody/tr[1]/td[12]')  # 第一张发票第一行的金额
first_invoice_data = '//*[@id="list"]/table/tbody/tr[%s]/td[4]'  # 第一张发票的其他行
total_amount = ('xpath', '//*[@id="list"]/table/tbody/tr[6]/td[5]')  # 金额合计
tax_amount = ('xpath', '//*[@id="list"]/table/tbody/tr[6]/td[7]')  # 税额合计
tax_total_price = ('xpath', '//*[@id="list"]/table/tbody/tr[6]/td[8]')  # 价税合计

invoice_money = '//tr[%s]//*[@name="amount"]'  # 发票详细的交易事项金额
invoice_total = ('xpath', '//*[@name="total_amount"]')
invoice_total_price = ('xpath', '//*[@name="total_vat"]')

invoice_amount = '//*[@id="list"]/table/tbody/tr[%s]/td[5]'
invoice_total_amount = '//*[@id="list"]/table/tbody/tr[%s]/td[7]'
invoice_price_amount = '//*[@id="list"]/table/tbody/tr[%s]/td[8]'

settlement = ('xpath', '//*[@id="list"]/table/tbody/tr[3]/td/div/div[4]/div/div[2]/div/table/tfoot/tr/td/button/span')
settlement_btn = ('xpath', '//*[@data-reactid=".1.0.2.0"]')
settlement_info = ('xpath', '//*[@id="list"]/table/tbody/tr[3]/td/div/div[4]/div/div[2]/div/table/tbody/tr/td[1]')
delete_settlement = ('xpath', '//*[@class="btn btn-danger js-remove"]')  # 删除结算按钮
delete_settlement_confirm = ('xpath', '//*[@class="btn btn-large btn-danger"]')
batch_settlement_btn = ('id', 'more-pljs')
batch_set_btn = ('xpath', '//*[@class="bulk-make-settlement-confirm btn btn-primary"]')
batch_settlement_confirm = ('xpath', '//*[@class="btn btn-primary confirm-done"]')
batch_set_info = ('xpath', '//*[text()="批量结算成功。"]')

create_vouch = ('xpath', '//*[@name="btn-23101004"]')  # 生成凭证
create_vouch_confirm = ('id', 'btn-register')  # 生成凭证的确认按钮
check_vouch = ('xpath', '//*[@class="reconciled"]')  # 检查凭证创建
check_vouch_num = ('xpath', '//tbody[1]//tr[1]//td[@class="pzzh-cell"]//a')  # 检查凭证字号
delete_vouch = ('id', 'more-scpz')  # 删除凭证
delete_vouch_confirm = ('id', 'btn-quxiaodengji')

collect = ('id', 'more-xxCaiji-new')  # 采集//*[@name="total_amount"]
collect_confirm = ('xpath', '//*[@class="btn btn-primary save-button close-trigger"]')  # 采集
check_xxfp_collect = ('xpath', '//div[@id="pager"]/div/span/label')  # 采集确认
refresh_btn = ('xpath', '//*[@onclick="javascript:refreshPage()"]')  # 页面刷新按钮

view_amount = ('xpath', '//*[@name="btn-23101005"]')  # 查看汇总
amount = '//*[@id="dataTable"]/tbody/tr[1]/td[%s]'  # 获得汇总信息

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

auto_create_inventory_element = [refresh_btn, select_all, batch_edit, auto_create, ipt_create, auto_create_tips,
                                 save_edit, subject_save, edit_confirm]
