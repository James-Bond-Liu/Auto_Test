# !@coding  :utf-8 
# !@Time    :2021/1/28 16:39
# !@Author  :LiuLei


deprecition_page = ('xpath', '//*[@link="/assets"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/assets"]')
page_refresh = ('xpath', '//*[@id="breadcrumb"]//*[@onclick="javascript:window.location.reload()"]')

add_asset = ('xpath', '//*[@name="btn-23410001"]')
delete_asset = ('id', 'deleteGdzcListBtn')
delete_confirm = ('xpath', '//*[@onclick="deleteAction()"]')
first_item_select_box = ('xpath', '//tbody//tr[1]//td[1]//input')
first_item_check = '//*[@class="main-container"]//tbody//tr[1]//td[%s]'  # 3~13
check_page = ('xpath', '//span[text()="大汽车"]')
# 新增资产界面
asset_type = ('xpath', '//*[@name="zcsx"]')
asset_coding = ('id', 'fixed_asset_zcbm')
asset_name = ('id', 'fixed_asset_name')
asset_start_use = ('id', 'acquisition_date_text')
asset_price = ('id', 'fixed_asset_gmjg')
asset_num = ('id', 'fixed_asset_qty')
asset_czl = ('id', 'fixed_asset_czl')
asset_month = ('id', 'asset_month')
asset_save_btn = ('xpath', '//*[@onclick="saveAction()"]')
asset_ignore = ('xpath', '//*[@value="忽略并保存"]')
asset_list = [asset_coding, asset_name, asset_start_use, asset_price, asset_num, asset_czl, asset_month]
# 编辑资产
asset_detail = ('xpath', '//*[@class="main-container"]//tbody//tr[1]//td[14]/span/a')
asset_edit = ('xpath', '//*[@onclick="edit_asset()"]')
