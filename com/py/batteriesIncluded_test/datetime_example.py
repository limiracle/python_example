#!/usr/bin/python
#coding=utf-8

import time
print time.time()#本地时间戳
print time.localtime()
print time.asctime(time.localtime(time.time()))#最简单的获取可读的时间模式的函数是asctime():

#使用 time 模块的 strftime 方法来格式化日期，
#time.strftime(format[, t])
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


#Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历
import calendar
cal=calendar.month(2016,7)
print cal



#注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类
#如果仅导入import datetime，则必须引用全名datetime.datetime。
from datetime import datetime
now=datetime.now()
print(type(now))
print now

dt=datetime(2015,4,15,12,30)
print(dt)

#很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print cday

print datetime.now().strftime('%a, %b %d %H:%M')

#对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import datetime,timedelta
print datetime.now()+timedelta(hours=10)
print datetime.now()-timedelta(days=2,hours=3)