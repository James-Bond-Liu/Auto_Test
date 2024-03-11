# -*- coding: utf-8 -*-
# @Time :2020/6/21 15:04
# @Author : liufei
# @File :ejfdilj.PY

import configparser
# 常用的配置文件后缀是.ini、.conf、.py，当然还有使用.json、.txt的，推荐使用常用的.ini、.py，配置文件的名字一般是config便于理解和使用。
#数据类型，无论是数字还是列表等数据类型，一旦进入配置文件就全部转换成字符串。
#可以利用eval()函数将格式转化成原本的数据格式

config = configparser.ConfigParser()
config.read(r"./config.ini", encoding="utf-8")

config.sections()  # 获取所有的section节点

config.options('mysql')  # 获取指定section 的options，即该节点的所有键

config.get("mysql", "name")  # 获取指定section下options下的value
config.getint("mysql", "proxy")  # 将获取到值转换为int型
config.getboolean("mysql", "pool")  # 将获取到值转换为bool型
config.getfloat("mysql", "time")  # 将获取到值转换为浮点型

config.items("mysql")  # 获取section的所有的配置信息

config.set("mysql", "name", "root")  # 修改db_port的值为69

config.has_section("mysql")  # 是否存在该section
config.has_option("mysql", "password")  # 是否存在该option

config.add_section("redis")  # 添加section节点
config.set("redis", "name", "redis_admin")  # 设置指定section 的options

config.remove_section("redis")  # 整个section下的所有内容都将删除
config.remove_option("mysql", 'time')  # 删除section下的指定options

config.write(open("config.ini", "w"))  # 保存config，此处打开文件方式选择”w“，并不会将文件的原始内容全部覆盖


