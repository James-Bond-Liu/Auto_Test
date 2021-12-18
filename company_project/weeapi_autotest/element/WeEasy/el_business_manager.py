# !@coding  :utf-8 
# !@Time    :2021/1/5 18:11
# !@Author  :LiuLei


"""
客户管理界面
"""
normal_filter = ('id', 'filter-qyzt-btn1')
block_filter = ('id', 'filter-qyzt-btn2')

add_business = ('xpath', '//*[@name="btn-20201001"]')  # 新增客户
import_btn = ('xpath', '//*[@name="btn-20201002"]')  # 导入客户
export_btn = ('xpath', '//*[@name="btn-20201010"]')  # 导出客户
collect_btn = ('xpath', '//*[@name="btn-20201003"]')  # 采集
collect_confirm = ('xpath', '//*[@id="notifier-confirm-custom-dialog"]/div/div/div[3]/div/input[1]')
batch_delete_btn = ('xpath', '//*[@name="btn-20201004"]')  # 批量删除

batch_block_btn = ('xpath', '//*[@name="btn-20201005"]')  # 批量停用
s_batch_block_btn = ('xpath', '//*[@onclick="enableCustomerAction()"]')

batch_unblock_btn = ('xpath', '//*[@name="btn-20201009"][contains(.,("批量启用"))]')  # 批量启用
s_batch_unblock_btn = ('xpath', '//*[@onclick="disenableCustomerAction()"]')

select_all_business = ('xpath', '//*[@class="checkbox-master"]')  # 全选
total = ('xpath', '//*[@id="table_page"]/div/div/span/label')
"""
新增客户弹窗
"""
ipt_business_name = ('id', 'qymc')  # 企业名称
select_province = ('id', 'province')  # 地区-省
select_city = ('id', 'city')  # 地区-市
select_county = ('id', 'county')  # 地区-市辖区
select_gs_dlfs = ('id', 'gs_dlfs')
select_gs_yzlx = ('id', 'gs_yzlx')
identity_num = ('id', 'gs_zjhm')  # 证件号码
telephone_num = ('id', 'gs_sjhm')  # 手机号码
gssb_pwd = ('id', 'grsds_wtjm_pwd')  # 个税申报密码

save_btn = ('xpath', '//*[@class="btn btn-primary save-button "]')  # 保存
save_add_btn = ('xpath', '//*[@class="btn btn-primary save-add-button"]')  # 保存并新增
cancel_btn = ('xpath', '//*[@class="btn btn-primary save-add-button"]//following-sibling::button')  # 取消

"""
客户操作栏
"""
edit_btn = ('xpath', '//*[@name="btn-20201007"]')  # 编辑

delete_btn = ('xpath', '//*[@name="btn-20201004"]')  # 删除
ipt_delete_pwd = ('id', 'password_fro_delete')
delete_confirm = ('xpath', '//*[@onclick="canDeleteCustomer()"]')
s_delete_btn = ('xpath', '//*[@id="tax_save"][@value="删除"]')

block_btn = ('xpath', '//*[@name="btn-20201005"]')  # 停用
s_block_btn = ('xpath', '//*[@onclick="enableSomeOneCustomerAction()"]')

unblock_btn = ('xpath', '//*[@name="btn-20201009"][text()="启用"]')  # 启用
s_unblock_btn = ('xpath', '//*[@onclick="enableCustomer("singleModal")"]')


remark_btn = ('xpath', '//*[@name="btn-20201008"]')  # 备注
enter_btn = ('xpath', '//*[text()="武汉良梦家政服务有限公司"]//following-sibling::td[10]/a[5]')  # 进入账套
# enter_btn2 = ('xpath', '//*[text()="广东华庸建筑装饰工程股份有限公司"]//following-sibling::td[10]/a[5]')  # 进入账套
enter_btn2 = ('xpath', '//*[text()="东莞市顺彩颜料有限公司"]//following-sibling::td[10]/a[5]')  # 进入账套

business_name1 = ('xpath', '//*[text()="武汉良梦家政服务有限公司"]')  # 客户信息-企业名称
business_name1_edit = ('xpath', '//*[text()="武汉良梦家政服务有限公司"]//following-sibling::td[10]//a[1]')
business_name1_enter = ('xpath', '//*[text()="武汉良梦家政服务有限公司"]//following-sibling::td[10]//*[@name="btn-20201008"]//following-sibling::a')  # 进入账套

business_last_name = ('xpath', '//*[@value="曾用名"]')
business_add_last_name = ('xpath', '//*[@value="新增"]')
business_ipt_cym_mc = ('id', 'cym_mc')
business_save = ('xpath', '//*[@onclick="saveCym()"]')
business_check_last_name = ('xpath', '//*[@id="cym_tbody"]//tr[2]//td[1]')

business_account_info = ('xpath', '/html/body/div[5]/div/div[1]/a[2]')
opentime = ('id', 'filter-zq')  # 启用期间
cost_check = ('xpath', '//*[@onclick="onCbhsbsChange1()"]')  # 成本核算选择是


account_info_save = ('id', 'commit')
account_save_tips = ('xpath', '//*[@id="header"]/div[2]/div/div[2]/div/div/span')

select_this = ('xpath', '//*[text()="武汉良梦家政服务有限公司"]//preceding-sibling::td[2]')
select_this2 = ('xpath', '//*[text()="东莞市顺彩颜料有限公司"]//preceding-sibling::td[2]')

business_name2 = ('xpath', '//*[text()="青岛友茂源食品科技有限公司"]')  # 客户信息-企业名称

business_name3 = ('xpath', '//*[text()="南京康阜廷贸易有限公司"]')  # 客户信息-企业名称

business_name4 = ('xpath', '//*[text()="河南弗尔格机械设备有限公司"]')  # 客户信息-企业名称
business_name4_block_btn = (
    'xpath', '//*[text()="河南弗尔格机械设备有限公司"]//following-sibling::td[10]//*[@name="btn-20201005"]')  # 停用

business_name5 = ('xpath', '//*[text()="杭州越隆建材有限公司"]')  # 客户信息-企业名称
business_name5_delete = ('xpath', '//*[text()="杭州越隆建材有限公司"]//following-sibling::td[10]//*[@name="btn-20201004"]')  # 删除

first_business_name = '//tbody[1]//tr[1]//td[3]'  # 客户信息-企业名称
business_name = '//tbody//tr[%s]//td[3]'
"""
采集
"""
collect_status = '//tbody//tr[%s]//td[6]'
