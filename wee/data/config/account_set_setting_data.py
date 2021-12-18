# !@coding:utf-8
# !@Time:2021/1/715:21
# !@Author:LiuLei
import os
"""
账套--设置
"""
bank_num = '111111'
bank_name = ['中国工商银行的账户', '中国农业银行的账户', '中国银行的账户']

com_go_name = ['往来1', '往来2', '往来3']

costomer_name = ['苏宁', '百度', 'Google']

product_name = ['项目1', '项目2', '项目3']

sections_name = ['部门1', '部门2', '部门3']

subject_name = ['科目1', '科目2', '科目3']

supplier_name = ['淘宝', '京东', '天猫']

tags_name = ['标签1', '标签2', '标签3']

assets_class = [['0001', '电子产品', '240', '10'], ['0002', '办公用品', '240', '10'], ['0003', '机械硬件', '240', '10']]

invoice_rule = ['武汉市南方药品有限公司', '九州通医药集团股份有限公司', '武汉市聚荣璟大药房有限公司']

qcye_upload = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\自动化测试数据\期初余额-湖北卫普拉斯食品有限公司6月.xlsx'
qcye_check = "期初余额10,000.0010,000.000.00"
qcye_check2 = "本年累计发生额2,400.002,400.000.00"
qcye_check3 = "设置期初余额"
qcye_check_clear_info = '数据清空成功！'

history_data = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\自动化测试数据\历史凭据-朝晨商贸凭证导入模板.xls'
history_check_import = "共[253]条"
history_check_delete = "共[0]条"
history_import_status = "导入成功:【253】条数据。"

"""
账套-业务处理
"""
xxfp_data = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\自动化测试数据\销项发票-11月销项.xls'

xxfp_s_data = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\自动化测试数据\七加一番星20201102.xlsx'
xxfp_import_check = '共[5]条'
xxfp_add_check = '共[10]条'
xxfp_collect_check = '共[100]条'
xxfp_auto_create = '批量编辑成功'

jxfp_data = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\自动化测试数据\进项发票-11月进项.xls'
jxfp_autocomple_data = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\自动化测试数据\2.xlsx'
jxfp_add_check = '共[11]条'
jxfp_check = '已登记'
jxfp_collect_check = '共[1]条'
jxfp_add_invoice_type = ['增值税专用发票', '增值税普通发票', '机动车销售统一发票', '通用机打发票', '通行费发票', '海关进口增值税专用缴款通知书', '农产品发票']
xxfp_add_invoice_type = ['增值税专用发票', '增值税普通发票', '机动车销售统一发票', '通用机打发票', '没有开具发票']

bill_select = '中国农业银行的账户'
bill_data = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\自动化测试数据\账单-杭州侏罗纪投资管理有限公司.xls'
bill_import_check = '共[519]条'
bill_clear_check = '共[0]条'
bill_register_check = '已登记'
bill_delete_register_check = '未登记'
bill_vouch_check = '记-1'

receipts_register_money = '100000'
receipts_register_check = '共[2]条'
receipts_register_detail_add_check = '共[5]条'
receipts_register_delete_check = '共[0]条'
receipts_register_set_tips = '选择的交易批量结算成功了。'
receipts_register_delete_tips = '选择的交易结算批量删除成功了。'

person_register_identity_card = ['350524198303062556', '350524198303062553', '350524198303062555']
person_register_name = ['一号员工', '二号员工', '三号员工']
person_register_phone = ['11111111111', '22222222222', '33333333333']
person_register_dimission = '2021-01-20'
person_register_birth = '1983-3-06'

person_register_edit = ['nsrzt', 'sfgy', 'fylx']
person_register_edit_value = ['2021-01-21', '21', '1001_库存现金']
person_register_edit_check = [['库存现金', '保险营销员', '2021-01-21'], ['库存现金', '保险营销员', '2021-01-21'],
                              ['库存现金', '保险营销员', '2021-01-21']]
person_register_data = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\自动化测试数据\薪酬-全部人员.xls'
person_register_import = '导入成功【3】条数据！'
history_upload = os.path.abspath(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + r'\测试数据\autoit\history_upload.exe'
register_person_upload = os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))) + r'\测试数据\autoit\register_person_upload.exe'

person_register_payroll = ['0101', '0102', '0103', '0401', '0402', 'scjyhd']
person_register_payroll_check = ['生产经营所得-核定征收', '正常工资薪金表', '外籍人员正常工资薪金', '全年一次性奖金收入', '劳务报酬(一般劳务、其他非连续劳务)',
                                 '劳务报酬(保险营销员、证券经纪人、其他连续劳务)']
payroll_type1_data = ['100000', '0.3', '50', '25', '50', '100']

payroll_type_data = ['10000', '100', '其他']

payroll_type1_check = ['14800', '0.05', '0', '740', '100.00', '减半征收']
payroll_type2_check = ['10,000.00', '0.00', '100.00', '100.00', '100.00', '100.00', '400.00', '100.00', '200.00',
                       '0.00', '9,300.00', '未同步', '其他']
payroll_type3_check = ['10,000.00', '100.00', '100.00', '260.00', '260.00', '9,740.00', '其他']
payroll_type4_check = ['10,000.00', '100.00', None, '0.00', '100.00', '294.00', '9,706.00', '其他']
payroll_type5_check = ['10,000.00', '100.00', '2,000.00', '1,520.00', '8,480.00', '其他']
payroll_type6_check = ['10000', '2000', '100', '5000', '3', '0', '0']

payroll_setting_check = '现金'
payroll_vouch_check = ['贰佰柒拾元整', '生成凭证']

additonal_deduction_children = ['牛夫人', '32012319950814321X', '2021-01-14', '五道口职业技术学院']
additonal_deduction_children_check = '共[1]条'
additonal_deduction_continue_education = ['2021-01-26', '3333', '国家游泳总局']
additonal_deduction_housing_loans = ['111111', '111111', '111111', '2021-01-15', '12', '111111', '2021-01-15', '12',
                                     '中国银行']
additonal_deduction_house_rents = ['2022-01-15', '2021-01-15', '北京']
additonal_deduction_care_old = ['100', '谢桂山', '341222195411227551', '1954-11-22']

deprecition = ['01111', '小汽车', '2019-11-30', '100000', '1', '5', '12']
deprecition_edit = ['01111', '大汽车', '2019-11-30', '200000', '1', '5', '14']
deprecition_check = ['2019-11-30', '01111', '小汽车', '固定资产', '电子产品', '100,000.00', '95,000.00', '395.83', '5,145.79',
                     '94,854.21']
deprecition_edit_check = ['2019-11-30', '01111', '大汽车', '固定资产', '电子产品', '200,000.00', '190,000.00', '791.67',
                          '11,875.05', '188,124.95']
deprecition_delete_check = '共[3]条'

inventory_type = ['存货类别1', '存货类别2', '存货类别3']
inventory_name = ['存货1', '存货2', '存货3']
inventory_unit = '个'
inventory_type_check = [['CHLB1', '存货类别1', '1405_库存商品'], ['CHLB2', '存货类别2', '1405_库存商品'],
                        ['CHLB3', '存货类别3', '1405_库存商品']]
inventory_count = '共[3]条'
delete_inventory_count = '共[2]条'
inventory_bom_check = [['BOM00001', '存货类别1', '厄贝沙坦氢氯噻嗪片'], ['BOM00002', '存货类别1', '医用冷敷贴（颈肩腰腿型）']]

cost_data = ['50', '1']
cost_check_data = ['恩替卡韦分散片', '0.5mg*14s*2板', '盒', '5.0000', '256.6380', '1,283.19', '1,283.19']
cost_check_info = '已完成'
