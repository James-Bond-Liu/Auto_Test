# !@coding  :utf-8 
# !@Time    :2021/1/7 16:10
# !@Author  :LiuLei

assets_class = ('xpath', '//*[@link="/assets/zclb"]')  # 资产类别功能页面
delete_check = ('xpath', '//*[text()="机械硬件"]')  # 选择一个资产类别
select_box = ('xpath', '//*[text()="机械硬件"]//preceding-sibling::td[2]')  # 资产类别的勾选框
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/assets/zclb"]')  # 切换至新的框架
refresh_page = ('xpath', '//*[@onclick="javascript:window.location.reload()"]')

add_assets_class = ('xpath', '//*[@name="btn-24215001"]')
ipt_assets_class_num = ('id', 's_zclbdm')
ipt_assets_class_name = ('id', 's_zclbmc')
ipt_swzclb = ('id', 's_swzclbdm_chosen')

select_swzclb = ('xpath', '//*[@data-option-array-index="5"]')

ipt_s_synx = ('id', 's_synx')
ipt_s_czl = ('id', 's_czl')
add_assets_class_confirm = ('xpath', '//*[@onclick="save()"]')
assets_class_name = '//div[@id="js-app-container"]/div/div[2]/table/tbody/tr[%s]/td[3]'

delete_assets_class = ('xpath', '//*[@name="btn-24215003"]')
delete_confirm = ('xpath', '//*[@data-reactid=".1.0.2.0"]')
