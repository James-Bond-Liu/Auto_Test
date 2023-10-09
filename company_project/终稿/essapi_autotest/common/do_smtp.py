import yagmail

# 连接服务器
# 用户名、授权码、服务器地址
yag_server = yagmail.SMTP(user='fei.liu@hxgroup.com', password=' U286G-WJEDM-X2VPX-YD9BR-3RFQV', host='smtp.partner.outlook.cn')
# 发送对象列表
email_to = ['fei.liu@hxgroup.com', ]
email_title = '测试报告'
email_content = "这是测试报告的具体内容"
# 附件列表
email_attachments = None
a = ['./attachments/report.png']
# 发送邮件
yag_server.send(email_to, email_title, email_content, email_attachments)
# 关闭连接
yag_server.close()

ding = "https://oapi.dingtalk.com/robot/send?access_token=6f1497f326c798aafc776d0a7db70b84de387bbc8b54e625764e12df477b16ae"
