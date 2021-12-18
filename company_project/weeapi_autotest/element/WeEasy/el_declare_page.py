# !@coding  :utf-8 
# !@Time    :2021/2/7 16:00
# !@Author  :LiuLei

# 企业列表
business_list_btn = ('xpath', '//*[@name="menu-22001"]')
business_check_page = ('xpath', '//li[text()="企业列表"]')
# 报表列表
statement_list_btn = ('xpath', '//*[@name="menu-22002"]')
statement_check_page = ('xpath', '//li[text()="报表列表"]')

page_list = [business_list_btn, statement_list_btn]
check_list = [business_check_page, statement_check_page]

# 申报
declare_btn = ('xpath', '//*[@name="btn-22002001"]')
declare_confirm = ('xpath', '//*[@value="继续申报"]')
declare_er = ('xpath', '//*[@id="XzjsModal"]//*[text()="确认"]')
# 扣款
payment_btn = ('xpath', '//*[@name="btn-22002002"]')
# 撤销申报
revocation_btn = ('xpath', '//*[@name="btn-22002003"]')
revocation_confirm = ('id', 'confirmButton')
# 设为零申报
set_zero_btn = ('xpath', '//*[@name="btn-22002004"]')
# 设为税款申报
set_tax_btn = ('xpath', '//*[@name="btn-22002005"]')
# 状态检查
check_status = ('xpath', '//*[@name="btn-22002006"]')
# 企业查询
business_filter = ('id', 'filter-qycx')
page_limt = ('xpath', '//*[@class="limit-select"]')
# 合计
total = ('xpath', '//*[@id="pager"]/div/span/label')
# 选择全部
select_all = ('xpath', '//*[@class="checkbox-master"]')
# 查看
view = '//tbody//tr[%s]//td[18]//*[contains(.,"查看")]'
# 申报状态
declare_status = '//tbody//tr[%s]//td[9]/span'
# 作废状态
invalid_status = '//tbody//tr[%s]//td[12]/span'
# 申报表名称
declare_name = '//tbody//tr[%s]//td[4]'
# 显示异常
show_error = ('id', 'filter-xsycyy')
# 撤销状态
fetch_status = '//tbody//tr[%s]//td[8]'
# 税款
pay_tax = '//tbody//tr[%s]//td[14]'
# 勾选框
select_box = '//tbody//tr[%s]//td[1]/input'
# 企业名称
name = '//tbody//tr[%s]//td[3]'
# 异常内容
error = '//tbody//tr[%s]//td[13]'
