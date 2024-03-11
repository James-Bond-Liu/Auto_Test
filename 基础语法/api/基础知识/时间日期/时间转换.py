import time
import datetime

"""时间戳转换为日期"""
# 方法一
print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y/%m/%d %H:%M:%S'))

# 方法二
now_timestamp = time.time()  # 获取当前时间的时间戳

# 时间戳先转成时间元组，strftime在转成指定格式
now_tuple = time.localtime(now_timestamp)
time.strftime("%Y/%m/%d %H:%M:%S", now_tuple)

"""日期时间转换为时间戳"""
date = "2020-12-26 11:45:34"

# 时间字符串转成时间数组形式
date_array = time.strptime(date, "%Y-%m-%d %H:%M:%S")

# 查看时间数组数据
print("时间数组：", date_array)

# mktime时间数组转成时间戳
time.mktime(date_array)
