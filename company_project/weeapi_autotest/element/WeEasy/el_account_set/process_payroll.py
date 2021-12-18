# !@coding  :utf-8 
# !@Time    :2021/1/22 17:13
# !@Author  :liulei

payroll_page = ('xpath', '//*[@link="/easypayroll/payroll_summary"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/easypayroll/payroll_summary"]')
vouch_iframe = ('xpath','//*[@src="/editvoucher#"]')
page_refresh = ('xpath', '//*[@id="breadcrumb"]//*[@onclick="javascript:window.location.reload()"]')
"""薪酬表"""
payroll = ('xpath', '//*[@name="btn-23401005"]')
add_payroll = ('xpath', '//*[@name="btn-23402001"]')  # 新增薪酬表
compensation_type = ('id', 'sdxm')  # 薪酬表类型 0101、0102、0103、0401、0402、scjyhd
pay_method = ('id', 'jsfs')  # value='1'  支付方式
save_payroll = ('id', 'create_sbcb_btn')  # 保存薪酬表

add_payroll_item = ('xpath', '//*[@href="javascript:showDialog()"]')  # 新建薪酬表人员
select_person = ('xpath', '//*[@onchange="selectChange()"]')  # 选择薪酬表人员
select_payroll_all_person = ('id', 'employee_all')
set_zero = ('xpath', '//*[@onclick="createEmployeePayroll()"]')  # 生成零工资
set_improper = ('xpath', 'improper')  # 设置人员非正常
return_btn = ('xpath', '//*[@class="inner"]//*[@href="/easypayroll/payroll_summary"]')  # 返回按钮
s_add_payroll_item = ('xpath', '//*[@class="list-header"]//*[@class="list-actions"][1]/button[1]')  # 0402的新建人员
s_return_btn = ('xpath', '//*[@class="list-actions"]//*[@href="/easypayroll/payroll_summary"]')  # 0402的返回按钮
check_payroll = '//*[@id="js-app-container"]//tbody//tr[%s]//td[2]'  # 检查薪酬表创建数据
"""薪酬表-工资表"""
# 生产经营所得-核定征收
type1_create_vouch = ('xpath', '//tr[1]//*[@name="btn-23402005"]')  # 生产凭证
null_price_tips = ('xpath', '//*[@class="notification-message"][contains(.,("人员工资数据全部为0"))]')  # 工资数据为0时生成凭证后的提示
vouch_total = ('xpath', '//*[@class="voucher_total_node"]')
vouch_save = ('id', 'saveVoucher')

type1_edit = ('xpath', '//*[text()="生产经营所得-核定征收"]/parent::td/following-sibling::td[8]//span')
type1_payroll_save = ('xpath', '//*[@href="javascript:showSaveDialog()"]')  # 保存
type1_save_confirm = ('xpath', '//*[@onclick="save()"]')
total_income = ('id', 'srze')  # 收入总额
taxable_income = ('id', 'yssdl')  # 应得税率
allocation = ('xpath', '//tbody//tr[1]//td[5]/input')  # 分配比例
deduction = ('xpath', '//tbody//tr[1]//td[7]//a/span')  # 专项扣除
endowment_insurance = ('xpath', '//*[@class="number ylbx"]')  # 专项扣除-养老保险
medical_insurance = ('xpath', '//*[@class="number ylobx"]')  # 专项扣除-医疗保险
unemployment_insurance = ('xpath', '//*[@class="number sybx"]')  # 专项扣除-失业保险
provident_fund = ('xpath', '//*[@class="number zfgjj"]')  # #专项扣除-住房公积金
deduction_save = ('xpath', '//*[@id="scjysd-zxkc-edit-dialog"]//*[@value="确认"]')  # 专项扣除保存

other = ('xpath', '//tbody//tr[1]//td[8]//a/span')  # 其他
endowment_other = ('xpath', '//*[@class="number syylbx"]')
deduction_other = ('xpath', '//*[@class="number qtkc"]')
other_save = ('xpath', '//*[@id="scjysd-qt-edit-dialog"]//*[@value="确认"]')

prepay = ('xpath', '//tbody//tr[1]//td[13]//input')  # 已预缴税额
check_type1 = '//tbody//tr[1]//td[%s]'  # 9~12

type_sre = ('id', 'sre')  # 收入 通用
type_qtqtfy = ('id', 'qtqtfy')  # 其他 通用
type_save = ('id', 'save')  # 保存 通用
type_mssd = ('id', 'mssd')  # 免税所得 通用
type_jmse = ('id', 'jmse')  # 减免税额 通用
type_bz = ('id', 'bz')
# 正常薪资表
type2_edit = ('xpath', '//*[text()="正常工资薪金表"]/parent::td/following-sibling::td[8]//span')
type2_person_edit = ('xpath', '//tbody//tr[1]//td[19]/a/i')

type2_prev_sre = ('id', 'prev_sre')
type2_prev_mssd = ('id', 'prev_mssd')
type2_ylbx = ('id', 'ylbx')
type2_qtnj = ('id', 'qtnj')
type2_dbyl = ('id', 'dbyl')
type2_ylobx = ('id', 'ylobx')
type2_sybx = ('id', 'sybx')
type2_zfgjj = ('id', 'zfgjj')
type2_list = [type2_ylbx, type2_qtnj, type2_dbyl, type2_ylobx, type2_sybx, type2_zfgjj, type_qtqtfy]

type2_prev_zxkc = ('id', 'prev_zxkc')
type2_prev_zxfjkc = ('id', 'prev_zxfjkc')
type2_prev_qtkc = ('id', 'prev_qtkc')
type2_prev_zykcdjze = ('id', 'prev_zykcdjze')
type2_prev_jmse = ('id', 'prev_jmse')

# 外籍人员正常工资薪金
type3_edit = ('xpath', '//*[text()="外籍人员正常工资薪金"]/parent::td/following-sibling::td[8]//span')
type3_person_edit = ('xpath', '//tbody//tr[1]//td[13]/a/i')
type3_sjjze = ('id', 'sjjze')

type3_list = [type_mssd, type_qtqtfy, type3_sjjze]

# 全年一次性奖金收入
type4_edit = ('xpath', '//*[text()="全年一次性奖金收入"]/parent::td/following-sibling::td[8]//span')
type4_person_edit = ('xpath', '//tbody//tr[1]//td[14]/a/i')
type4_list = [type_mssd, type_qtqtfy]
# 劳务报酬（一般劳务、其他非连续劳务）
type5_edit = ('xpath', '//*[text()="劳务报酬(一般劳务、其他非连续劳务)"]/parent::td/following-sibling::td[8]//span')
type5_person_edit = ('xpath', '//tbody//tr[1]//td[13]/a/i')
type5_qtsyjkbx = ('id', 'qtsyjkbx')
type5_zykcjze = ('id', 'zykcjze')

type5_list = [type_mssd, type5_qtsyjkbx, type_qtqtfy, type5_zykcjze]
# 劳务报酬(保险营销员、证券经纪人、其他连续劳务)
type6_edit = ('xpath', '//*[text()="劳务报酬(保险营销员、证券经纪人、其他连续劳务)"]/parent::td/following-sibling::td[8]//span')
type6_person_edit = ('xpath', '//tbody//tr[1]//td[14]/a/i')
type6_prevsre = ('id', 'prevSre')
type6_prevmssr = ('id', 'prevMssr')
type6_syjkbx = ('id', 'syjkbx')
type6_qt = ('id', 'qt')
type6_yxkcdsf = ('id', 'yxkcdsf')
type6_prevqtkc = ('id', 'prevQtkc')
type6_zykcdjze = ('id', 'zykcdjze')

type6_list = [type_mssd, type6_syjkbx, type6_qt, type6_yxkcdsf, type6_zykcdjze, type_jmse]

"""薪酬表设置"""
# 正常工资薪资表
type2_set = ('xpath', '//*[text()="正常工资薪金表"]/parent::td/following-sibling::td[10]')
jsfs_setting = ('id', 'jsfs_setting')
setting_confirm = ('xpath', '//*[@onclick="saveSetting()"]')
pay_method_check = ('xpath', '//*[text()="正常工资薪金表"]/parent::td/following-sibling::td[6]')
