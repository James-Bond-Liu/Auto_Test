# !@coding  :utf-8 
# !@Time    :2021/1/25 15:45
# !@Author  :liulei

payroll_page = ('xpath', '//*[@link="/zxfjkc/index"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/zxfjkc/index"]')
page_refresh = ('xpath', '/html/body/div[5]/div[1]/button')

add_btn = ('xpath', '//*[@name="btn-23403002"]')
delete_btn = ('xpath', '//*[@name="btn-23403003"]')
# 子女教育支出

children_education = ('xpath', '//*[@data-code="znjy"]')
xm_chosen = ('id', 'xm_chosen')
select_xm = ('xpath', '//*[@class="chosen-results"]//li[3]')

add_child = ('xpath', '//*[@id="detailModel"]/div/div/div[3]/div[7]/button[1]')
child_name = ('xpath', '//*[@name="znxm"]')
child_identity_type = ('xpath', '//*[@name="znzzlx"]')  # value = 201
child_identity_card = ('xpath', '//*[@name="znzzhm"]')
state_chosen = ('xpath', '//*[@name="zngjdq"]')  # value = 156
child_education_type_chosen = ('xpath', '//*[@name="sjyjd"]')  # value = 40
start_education = ('xpath', '//*[@name="sjyrqq"]')
end_education = ('xpath', '//*[@name="sjyrqz"]')
attend_country = ('xpath', '//*[@name="jdgjdq"]')  # value = 156
attend_school = ('xpath', '//*[@name="jdxx"]')
save_btn = ('xpath', '//*[@class="modal-footer"]//*[@class="btn btn-primary"][text()="保存"]')
check_add = ('xpath', '//*[@id="app"]//*[@class="sw-pagination"]//label')
child_list = [add_btn, xm_chosen, select_xm, add_child]
# 继续教育支出
continue_education = ('xpath', '//*[@data-code="jxjy"]')
con_educa_type = ('xpath', '//*[@name="jxjylx"]')  # value = 21
con_educa_name = ('xpath', '//*[@name="zsmc"]')
issue_date = ('xpath', '//*[@name="zsqdsj"]')
certificate_name = ('xpath', '//*[@name="zsmc"]')  # value = 20401
certificate_num = ('xpath', '//*[@name="zsbh"]')
issue_p = ('xpath', '//*[@name="fzjg"]')
edu_list = [issue_date, certificate_num, issue_p]
# 住房贷款利息支出
housing_loans = ('xpath', '//*[@data-code="zfdk"]')
build_num = ('xpath', '//*[@id="detailModel"]/div/div/div[3]/div[6]/div[2]/div[2]/input')
house_type = ('xpath', '//*[@name="fwzslx"]')  # value = 01
house_num = ('xpath', '//*[@id="detailModel"]/div/div/div[3]/div[6]/div[4]/div[2]/input')
contract_num = ('xpath', '//*[@id="detailModel"]/div/div/div[3]/div[7]/div[2]/div[2]/input')
first_repayment = ('id', '0_schkrq')
loan_periods = ('id', '0_dkqx')
contract_num2 = ('xpath', '//*[@id="detailModel"]/div/div/div[3]/div[7]/div[9]/div[2]/input')
first_repayment2 = ('id', '1_schkrq')
loan_periods2 = ('id', '1_dkqx')
loan_bank = ('xpath', '//*[@id="detailModel"]/div/div/div[3]/div[7]/div[12]/div[2]/input')

house_list = [build_num, house_num, contract_num, first_repayment, loan_periods, contract_num2, first_repayment2,
              loan_periods2, loan_bank]
# 住房租金支出
housing_rents = ('xpath', '//*[@data-code="zfzj"]')
select_city = ('xpath', '//*[@name="gzcs"]/following-sibling::div/a')  # value = 110100
city_choose = ('xpath', '//ul//*[text()="北京市"]')
lessor_type = ('xpath', '//*[@name="czflx"]')

house_position = ('xpath', '//*[@name="fwxxdz"]')
house_start_time = ('xpath', '//*[@name="zlrqq"]')
house_end_time = ('xpath', '//*[@name="zlrqz"]')
house = [add_btn, xm_chosen, select_xm, add_child, select_city, city_choose]
house_rents_list = [house_end_time, house_start_time,house_position]
# 赡养老人支出
care_old = ('xpath', '//*[@data-code="sylr"]')
share_type = ('xpath', '//*[@name="ftfs"]')  # value=3
share_money = ('id', 'bndykcje')
add_older = ('xpath', '//*[@id="detailModel"]/div/div/div[3]/div[8]/button[1]')
older_name = ('xpath', '//td//*[@name="xm"]')
older_identity = ('xpath', '//*[@name="zzlx"]')  # value = 201
older_identity_num = ('xpath', '//td//*[@name="zzhm"]')
older_country = ('xpath', '//*[@name="gjdq"]')  # value = 156
older_relation = ('xpath', '//*[@name="ynsrgx"]')  # value = 5
older_birth = ('xpath', '//td//*[@name="csrq"]')
older_list = [add_btn, xm_chosen, select_xm, add_older]
older_select = [share_type, older_identity, older_country, older_relation]
older_send = [share_money, older_name, older_identity_num, older_birth]
