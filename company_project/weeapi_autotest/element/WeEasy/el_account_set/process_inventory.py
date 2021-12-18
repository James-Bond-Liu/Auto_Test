# !@coding  :utf-8 
# !@Time    :2021/1/29 13:58
# !@Author  :LiuLei

inventory_page = ('xpath', '//*[@link="/company/inventory"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/company/inventory"]')
page_refresh = ('xpath', '//*[@id="breadcrumb"]//*[@onclick="javascript:window.location.reload()"]')

inventory = ('xpath', '//*[@id="content-page"]//*[text()="存货"]')
inventory_type = ('xpath', '//*[@id="content-page"]//*[text()="存货类别"]')
inventory_bom = ('xpath', '//*[@id="content-page"]//*[text()="BOM单"]')
# 新增存货类别
add_inventory_type = ('xpath', '//*[@name="btn-24207008"]')
ipt_type_name = ('id', 'chlbmc')
ipt_type_coding = ('id', 'chlbdm')
select_type_sections = ('id', 'kmuuid')  # value = '1405_库存商品'
save_inventory_type = ('xpath', '//*[@onclick="saveChlb()"]')
add_type_check = '//tbody[1]//tr[%s]//td[%s]'  # 1,3, 3,6

# 存货
add_inventory = ('xpath', '//*[@name="btn-24207004"]')
delete_inventory = ('xpath', '//*[@name="btn-24207003"]')
delete_confirm = ('xpath', '//*[@class="modal-open"]//*[@class="btn btn-primary confirm-custom-dialog-confirm-btn"]')
inventory_name = ('id', 'chmc')
inventory_select_type = ('id', 'ch_chlbdm')  # value = ’存货类别1‘
inventory_unit = ('id', 'chdw')
save_add_inventory = ('xpath', '//*[@onclick="saveCh()"]')
add_inventory_check = '//tbody[1]//tr[1]//td[%s]'  # 3,6
inventory_count = ('xpath', '//*[@id="content-page"]//span/label')
inventory_filter = ('xpath', '//*[@class="pull-right"]//select')  # 存货界面 select_value = 50
select_inventory = ('xpath', '//td[text()="存货3"]/preceding-sibling::td[5]')

# bom单
add_inventory_bom = ('xpath', '//*[@name="btn-24207011"]')
delete_inventory_bom = ('xpath', '//*[@name="btn-24207010"]')
ipt_bom_type = ('xpath', '//*[@name="chlbuuid"]/following-sibling::div')
select_bom_type = ('xpath', '//*[@name="chlbuuid"]/following-sibling::div//*[text()="存货类别1"]')
ipt_bom_product = ('xpath', '//*[@name="chuuid"]/following-sibling::div')
select_bom_product = ('xpath', '//*[@name="chuuid"]/following-sibling::div//*[text()="厄贝沙坦氢氯噻嗪片"]')
select_bom_product2 = ('xpath', '//*[@name="chuuid"]/following-sibling::div//*[text()="医用冷敷贴（颈肩腰腿型）"]')
bom_add = ('xpath', '//a[text()="增加"]')
bom_name = '//tbody[1]//tr[%s]//td[3]/div'
bom_item = '//td//*[@class="chosen-drop"]/ul/li[%s]'  # 2~6
bom_num = '//tr[%s]//*[@name="sl"]'  # send_key 1
save_bom = ('xpath', '//*[@class="btn btn-primary"][text()="保存"]')
check_item = '//tbody//tr[%s]//td[%s]'  # 3~6
select_box = '//tbody//tr[%s]//td[1]/input'
bom_elements = [add_inventory_bom, ipt_bom_type, select_bom_type, ipt_bom_product, select_bom_product]
