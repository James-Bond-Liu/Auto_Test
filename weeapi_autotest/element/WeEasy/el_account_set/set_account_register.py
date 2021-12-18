# !@coding  :utf-8 
# !@Time    :2021/1/7 10:29
# !@Author  :liulei

zhdj = ('xpath', '//*[text()="账户登记"]')  # 账户登记
add_account = ('xpath', '//*[@class="actions"]//*[@name="btn-24201001"]//*[contains(.,("新建账户"))]')  # 新建账户


ipt_bank = ('xpath', '//*[@class="chosen-single chosen-default"]')  # 银行选择框
bank_type1 = ('xpath', '//*[@data-option-array-index="1"]')  # 第一个银行
bank_type2 = ('xpath', '//*[@data-option-array-index="2"]')  # 第二个银行
bank_type3 = ('xpath', '//*[@data-option-array-index="3"]')  # 第三个银行
account_num = ('id', 'zh')  # 银行账户
account_name = ('id', 'zhjc')  # 账户名称
save = ('id', 'save')  # 保存按钮
get_bank_name1 = 'xpath'
get_bank_name2 = '//tbody[@id="yhzhList"]//tr[%s]//td[1]'  # 账户登记-银行账户名称

delete_btn = ('xpath', '//*[text()="中国银行的账户"]//following-sibling::td[6]//a//i')
delete_bank_info = ('xpath', '//*[text()="中国银行的账户"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/walletables"]')  # 切换html框架
