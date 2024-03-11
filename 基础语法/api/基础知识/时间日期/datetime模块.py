import datetime
"""主要记录datetime模块下datetime类的使用方法

datetime.today()：返回一个表示当前本地时间的datetime对象；
datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
datetime.utcnow()：返回一个当前utc时间的datetime对象；#格林威治时间
datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
datetime.combine(date, time)：根据date和time，创建一个datetime对象；
datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；
datetime对象.datetime.strftime(format)：将datetime对象转换为指定字符串格式时间
"""

# 格式化输出日期
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 2022-07-06 14:02:21

print("现在的时间是：",datetime.datetime.today())

print("返回现在的时间是：",datetime.datetime.now())

print("当前UTC日期和时间是：",datetime.datetime.utcnow())

print("时间戳的日期和时间是：",datetime.datetime.fromtimestamp(1234567896))

print("对应UTC时间戳的日期和时间是：",datetime.datetime.utcfromtimestamp(1234567896))

print("公历序列对应的日期和时间是：",datetime.datetime.fromordinal(1))

print("日期和时间的合体为：",datetime.datetime.combine(datetime.date(2020, 8, 31), datetime.time(12, 12, 12)))

now = datetime.datetime(2020,8,31,12,10,10)  # datetime对象
print("年为：",now.year)
print("月为：",now.month)
print("日为：",now.day)
print("小时为：",now.hour)
print("分钟为：",now.minute)
print("秒数为：",now.second)
print('当前日期为:', now.date() )
print('当前时间:', now.time() )
print("返回struct_time为",now.timetuple())   
print("返回UTC的struct_time为",now.utctimetuple())
print("返回的公历序列数为：",now.toordinal())   
print("返回标准日期格式为：",now.isoformat())
print("返回的周几(1表示周一)：",now.isoweekday())
print("返回的周几(0表示周一)：",now.weekday())      
print("now.isocalendar():", now.isocalendar())  
print("now.ctime():",now.ctime())
print("格式化时间为：",now.strftime('%Y/%m/%d %H:%M:%S'))   #  把日期按照format指定的格式进行格式化
print(datetime.datetime.strptime("2020/12/29 8:8:00",'%Y/%m/%d %H:%M:%S'))     #   将字符串格式转换为日期格式

"""timedelta类,时间加减
使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。"""

from  datetime import datetime, timedelta

dt = datetime.now()
#日期减一天
dt1 = dt + timedelta(days=-1)#昨天
dt2 = dt - timedelta(days=1)#昨天
dt3 = dt + timedelta(days=1)#明天
delta_obj = dt3-dt
print (type(delta_obj), delta_obj)  # <type 'datetime.timedelta'> 1 day, 0:00:00
print (delta_obj.days, delta_obj.total_seconds())  # 1 86400.0