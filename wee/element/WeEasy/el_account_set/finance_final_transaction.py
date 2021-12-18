# !@coding  :utf-8 
# !@Time    :2021/4/3 13:34
# !@Author  :LiuLei

fiscal_period = ('id', 'kjqj_header')
payment_days = '//*[text()="%s月"]/parent::li/preceding-sibling::li[1]/a'
final_page = ('xpath', '//*[@link="/yearEndInventory"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/yearEndInventory"]')
jzbtn = ('id', 'jzBtn')
jz_confirm = ('xpath', '//*[@name="commit"][@onclick="checkJtzj()"]')
