# !@coding  :utf-8 
# !@Time    :2021/1/6 15:28
# !@Author  :liulei
"""
首页
"""
jxfp = ('xpath', '//*[@class="action-link"][contains(.,(进项发票"))]')
xxfp = ('xpath', '//*[@class="action-link"][contains(.,("销项发票"))]')

ksdj = ('xpath', '//*[@class="action-link"][contains(.,("快速登记"))]')
zdyl = ('xpath', '//*[@class="action-link"][contains(.,("账单一览"))]')
zhyl = ('xpath', '//*[@class="action-link"][contains(.,("账户一览"))]')

sr = ('xpath', '//*[@class="action-link"][contains(.,("收入"))]')
zc = ('xpath', '//*[@class="action-link"][contains(.,("支出"))]')
zz = ('xpath', '//*[@class="action-link"][contains(.,("转账"))]')

ywcl = ('xpath', '//span[contains(.,"业务处理")]')
finance = ('xpath', '//span[contains(.,"财务")]')
form = ('xpath', '//span[contains(.,"报表")]')
setting = ('xpath', '//li[5]//*[@id="header-nav-settings"]')  # 设置
