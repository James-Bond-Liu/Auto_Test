# !@coding  :utf-8 
# !@Time    :2021/1/15 14:51
# !@Author  :liulei

receipts_register = ('xpath', '//*[@link="/deals/receipts_register"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/deals/receipts_register"]')

page_refresh = ('xpath', '//*[@onclick="javascript:window.location.reload()"]')

unsettled = ('xpath', '//*[@data-status="unsettled"]')
settled = ('xpath', '//*[@data-status="settled"]')

income_filter = ('xpath', '//*[@data-code="income"]')
expense_filter = ('xpath', '//*[@data-code="expense"]')
date = ('id', 'deal-form-settlement-date')
ipt_transaction = ('xpath', '//*[@name="account_item"]')
select_expense_transaction = ('xpath', '//*[@class="fcb-text"]//*[text()="库存商品"]')
ipt_costomer = ('xpath', '//*[@name="khgys_input"]')
select_costomer = ('xpath', '//*[@class="field"]/div[1]//*[@class="ac_over combobox-line"]/div[1]/div[2]')
select_income_transaction = ('xpath', '//*[@class="fcb-text"]//*[text()="收到应收账款"]')
ipt_money = ('id', 'deal-form-amount')

register_btn = ('id', 'submit')
register_check = ('xpath', '//*[@id="pager"]/div/span/label')

ipt_edit_detail = ('id', 'edit_detail')
detail_unsettled = ('xpath', '//*[@class="pull-left"]//*[@data-status="unsettled"]')
detail_settled = ('xpath', '//*[@class="pull-left"]//*[@data-status="settled"]')

detail_income = ('xpath', '//*[@class="clearfix"]//*[@data-code="income"]')
detail_expense = ('xpath', '//*[@class="clearfix"]//*[@data-code="expense"]')

detail_costomer = ('xpath', '//*[@class="partner_tagbox"]//input')
detail_select_costomer_type = ('xpath', '//*[@data-code="partner_customer"]')
detail_select_costomer = ('xpath', '//*[@class="item-name"]//*[text()="武汉市聚荣璟大药房有限公司艺境店【客户】"]')
detail_transaction = ('xpath', '//*[@class="fcb-container"]//div//input[@name="account_item"]')
detail_select_transaction = ('xpath',
                             '/html/body/div[12]/div/div/div/div[3]/div/div/div/table/tbody/tr/td[1]/div/div/div[2]/div/ul/li[1]/ul/li[1]/div[1]/div/div[3]/div[1]')
detail_amount = ('xpath', '//*[@class="cell-amount"]//*[@name="amount"]')
detail_save_btn = ('xpath', '//*[@class="header-buttons"]//*[@class="btn btn-primary"]')

select_all = ('xpath', '//*[@value="bulk-editor-toggle-all"]')
batch_set_btn = ('xpath', '//*[@name="btn-23301002"]')
ipt_set_date = ('xpath', '//*[@class="field"]//*[@name="payment_date"]')

set_btn = ('xpath', '//*[@class="bulk-make-settlement-confirm btn btn-primary"]')
set_confirm = ('xpath', '//*[@class="btn btn-primary confirm-done"]')
delete_set = ('xpath', '//*[@class="bulk-destroy-settlement-confirm btn btn-danger"]')
delete_set_confirm = ('xpath', '//*[@class="btn btn-primary confirm-done"]')
tips = ('xpath', '//*[@class="fixed-contents top-fixed"]//*[@class="notification-message"]')
check_page = ('xpath', '//*[@id="deals"]//*[@id="pager"]/div/span/label')

delete_receipts = ('xpath', '//*[@name="btn-23301003"]')
delete_receipts_confirm = ('xpath', '//*[@class="bulk-destroyer-confirm btn btn-large btn-danger"]')
