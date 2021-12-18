# !@coding  :utf-8 
# !@Time    :2021/1/7 19:38
# !@Author  :liulei

qcye_set = ('xpath', '//*[@link="/company/opening_balances"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/opening_balances"]')

ipt_qcye = ('xpath', '//*[@onclick="new_upload()"]')
upload = ('xpath', '//*[@class="fake-input"]//*[@class="input-file-ch-sa"]')

next_step = ('xpath', '//*[@onclick="yhzhCheck()"]')

check_page = ('xpath', '//*[@class="introduction-message"]')

ssph_btn = ('xpath', '//*[@name="btn-24101005"]')

get_ssph_info = ('xpath', '//*[@data-reactid=".1.0.0.0.1.1.0"]')
get_ssph_info2 = ('xpath', '//*[@data-reactid=".1.0.0.0.1.1.1"]')
close_ssph = ('xpath', '//*[@data-reactid=".1.0.0.1.0.0"]')
save_btn = ('xpath', '//*[@name="btn-24101006"]')
clear_data = ('id', 'clearDataBtn')
clear_confirm = ('xpath', '//*[@onclick="clearBalabce()"]')

clear_success = ('xpath', '//*[text()="数据清空成功！"]')

set_qcye_btn = ('xpath', '//*[text()="设置期初余额"]')
