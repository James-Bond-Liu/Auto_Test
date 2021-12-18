# !@coding  :utf-8 
# !@Time    :2021/1/11 16:28
# !@Author  :liulei

swbb = ('xpath', '//*[@link="/sbwcqk/detail/company"]')
change_iframe = ('xpath', '//*[@class="main-iframe"][@src="/sbwcqk/detail/company"]')

zzs_select_box = ('xpath', '//tbody[1]//tr[1]//*[@class="checkbox_td_1"]')
zzs_qushu = ('xpath', '//tr[1]//*[@name="btn-23702005"]')
zzs_sk = ('xpath', '//tbody[1]//tr[1]//*[@class="sk-item-cell number"]')
zzs_view = ('xpath', '//*[@id="list_1"]//tbody[1]//tr[1]//td[13]//*[@name="btn-23702006"]')


fjs_select_box = ('xpath', '//tbody[1]//tr[2]//*[@class="checkbox_td_1"]')
fjs_qushu = ('xpath', '//tbody[1]//tr[2]//td[13]//a[1]')
fjs_sk = ('xpath', '//tbody[1]//tr[2]//*[@class="sk-item-cell number"]')

select_all = ('xpath', '//*[@id="bb"]//*[@value="bulk-editor-toggle-all"]')
select_sk = '//tbody[1]//tr[%s]//*[@class="sk-item-cell number"]'
qushu = '//tbody[1]//tr[%s]//td[13]//a[1]'
sk = '//tbody[1]//tr[%s]//*[@class="sk-item-cell number"]'

check_tips = ('xpath', '//*[text()="取数成功"]')

page_refresh = ('xpath', '//*[@id="breadcrumb"]//*[@onclick="javascript:window.location.reload()"]')
sb = ('xpath', '//*[@class="an_sb_1 btn btn-small btn-primary"]//*[@data-help="bulkupdate"]')
sb_confim = ('xpath', '//*[@value="继续申报"]')
sb_status = '//tbody[1]//tr[%s]//td[7]'
