# !@coding  :utf-8 
# !@Time    :2021/1/20 11:05
# !@Author  :LiuLei


people_register = ('xpath', '//*[@link="/easypayroll/employee_management"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/easypayroll/employee_management"]')

page_refresh = ('xpath', '//*[@id="breadcrumb"]//*[@onclick="javascript:window.location.reload()"]')

"""功能按钮"""
delete_person = ('xpath', '//*[@name="btn-23401001"]')
add_cisborder_person = ('xpath', '//*[@name="btn-23401002"]')
add_overseas_person = ('xpath', '//*[@name="btn-23401003"]')
edit_person = ('xpath', '//*[@name="btn-23401004"]')

"""添加人员中的数据"""
person_status = ('id', 'nsrzt')
person_identity_card = ('id', 'zzhm')
person_name = ('id', 'xm')
person_sex = ('id', 'xb')
person_birth = ('id', 'csny')
dimission_date = ('id', 'lzrq')
partner_status = ('id', 'sfgd')
person_phone = ('id', 'lxdh')

"""添加境外人员中的数据"""
person_nationality = ('id', 'gj_chosen')  # select value=004
select_nationality = ('xpath', '//*[@id="gj_chosen"]//*[@data-option-array-index="1"]')
person_birth_place = ('id', 'csd_chosen')  # select value=004
select_birth_place = ('xpath', '//*[@id="csd_chosen"]//*[@data-option-array-index="1"]')
first_inbound = ('id', 'scrjsj')
departure = ('id', 'yjljsj')
reason = ('id', 'sssy_chosen')  # select value=10
select_reason = ('xpath', '//*[@id="sssy_chosen"]//*[@data-option-array-index="0"]')

"""保存"""
save_btn = ('xpath', '//*[@class="fields "]//*[@value="保存"]')
tips_confirm = ('xpath', '//*[@onclick="saveAsBdm()"]')
save_continue = ('xpath', '//*[@value="继续保存"]')

"""保存后的检查项"""
last_person_check = ('xpath', '//tbody[last()]//tr[last()]//td[3]')
second_person_check = ('xpath', '//tbody[last()]//tr[2]//td[3]')

"""批量修改"""
select_all = ('xpath', '//th[1]//*[@type="checkbox"]')

# nsrzt: 人员状态,sfgy:任职受雇从业类型,fylx:费用类型
edit_property = ('xpath', '//*[@onchange="batchAttributeChange()"]')  # 待修改属性
edit_save = ('xpath', '//*[@onclick="batchSave()"]')
tips_save = ('xpath', '//*[@value="保存"]')

nsrzt_date = ('xpath', '//*[@id="batch_update_rzsgrq"]')
person_type = ('id', 'sfgy')  # value='21'
money_type = ('id', 'fylx')  # text ='1001_库存现金'
edit_check = '//tbody[1]//tr[%s]//td[%s]'  # s1:1-4,  s2:8-11

last_person_edit = ('xpath', '//tbody[last()]//tr[3]/td[3]//preceding-sibling::td[2]//input')

"""删除"""
second_person_delete = ('xpath', '//tbody[last()]//tr[2]/td[3]//preceding-sibling::td[2]//input')
delete_confirm = ('xpath', '//*[@class="btn btn-large btn-danger"]')

"""导入"""
import_menu = ('xpath', '//*[text()="导入/导出"]')
import_btn = ('xpath', '//*[@href="javascript:showDialogImport();"]')
choose_file = ('xpath', '//*[@name="file"]')
upload_btn = ('id', 'uploadBtn')
import_tips = ('xpath', '//*[@class="notification success"]//*[@class="notification-message"]')
