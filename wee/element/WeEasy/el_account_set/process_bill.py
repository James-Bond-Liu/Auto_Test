# !@coding  :utf-8 
# !@Time    :2021/1/8 10:20
# !@Author  :liulei

bill = ('xpath', '//*[@link="/wallet_txns"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/wallet_txns"]')

select_account = ('id', 'relationWalletable')

"""导入"""
ipt_bill = ('xpath', '//*[@name="btn-23202002"]')
upload = ('xpath', '//*[@class="input-file-ch-sa"]')
next_step = ('xpath', '//*[@onclick="handleSubmit()"]')

# tips = ('xpath', '//*[text()="ok"]')
# confirm = ('xpath', '//*[@class="btn btn-default"][text()="确定"]')

check_page = ('xpath', '//*[@id="wallet-txn-list-page"]//*[@class="sw-pagination"]//span')

select_all = ('xpath', '//*[@value="bulk-editor-toggle-all"]')
more_func = ('xpath', '//*[text()="更多功能"]')
more_delete = ('id', 'more-delete')
delete_confirm = ('xpath', '//*[@class="btn btn-small btn-primary js-submit-btn btn-danger"]')

all_filter = ('xpath', '//*[@id="filter-entry-side"]//button[1]')
income_filter = ('xpath', '//*[@value="income"]')
expense_filter = ('xpath', '//*[@value="expense"]')
page_limit = ('xpath', '//*[@name="per-page"]')

income_money = '//*[@class="wallet-txn-list-table"]//tbody/tr[%s]/td[6]'  # 收入金额1，275
expense_money = '//*[@class="wallet-txn-list-table"]//tbody/tr[%s]/td[7]'  # 收入金额1，246

"""汇总"""
view_amount = ('xpath', '//*[@name="btn-23202005"]')
amount_income = ('xpath', '//*[@id="dataTable"]//tbody/tr[1]/td[4]')  # 汇总数据5，7
amount_expense = ('xpath', '//*[@id="dataTable"]//tbody/tr[1]/td[5]')  # 汇总数据5，7

"""登记"""
batch_register = ('xpath', '//*[@value="hebingdengji"]')
ipt_transaction = ('xpath', '//*[@name="account_item"]')
select_transaction = ('xpath', '//*[text()="收到应收账款"]')
register_btn = ('xpath', '//*[@class="btn btn-primary reconcile"]')
check_register_status = ('xpath', '//*[@id="list"]/table/tbody/tr[1]/td[10]/span')
delete_register = ('id', 'more-qxdj')
delete_register_confirm = ('xpath','//*[@class="btn btn-small btn-primary js-submit-btn submit-btn"]')

"""凭证"""
batch_vouch = ('xpath', '//*[@name="btn-23202004"]')
vouch_confirm = ('xpath', '//*[@class="btn btn-small btn-primary js-submit-btn submit-btn"]')
check_vouch_status = ('xpath', '//*[@id="list"]/table/tbody/tr[1]/td[11]/a')
delete_vouch_confirm = ('id', 'more-scpz')
