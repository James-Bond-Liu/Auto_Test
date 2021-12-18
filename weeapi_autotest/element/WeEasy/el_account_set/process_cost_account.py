# !@coding  :utf-8 
# !@Time    :2021/4/2 17:50
# !@Author  :LiuLei

"""成本核算"""
cost = ('xpath', '//*[@link="/cbhs/index"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/cbhs/index"]')

sccbhs = ('id', 'status_parent_sc')
xscbhs = ('id', 'status_parent')
rest_save = ('id', 'rest_save')
cost_confirm = ('xpath', '//*[@onclick="submitHsff()"]')
next_step = ('xpath', '//*[@class="pull-right"]//*[@class="btn btn-primary"][text()="下一步"]')
notify_tips = ('xpath', '//*[@class="notification-message"][text()="保存成功"]')
last_tips = ('xpath', '//span[@class="notification-message"][text()="生成出入库单成功！"]')
choose_product = ('xpath', '//*[text()="选择完工产品"]')
select_product = '//*[@class="Tbody"]//tr[%s]//td[1]'  # 1~3
select_confirm = ('xpath', '(//*[@class="btn btn-primary confirm-btn"][contains(.,"确认")])[2]')
ipt_num = '//table[1]//*[@class="co"]/tr[%s]/td[11]/input'  # 1
apportion = ('xpath', '//tr[2]//input[@name="ftl"]')  # 分摊率50
cost_completed = ('xpath', '(//*[@class="btn btn-primary"][contains(.,"完成")])[1]')

check_info = ('id', 'status_sc')
check_data = '//tbody[@class="co"]//tr[1]//td[%s]'  # 7~13
