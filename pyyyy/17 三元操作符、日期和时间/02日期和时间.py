# 时间模块
import time
# 日期模块
import calendar

# 时间戳（1970年1月1日午夜【历元】到现在经过的秒数）
# print(time.time())

# 获取本地时间
# print(time.localtime())

# 获取本地时间（更易读）
# print(time.asctime())

# 获取自定义时间
# %y获取两位数年份
# %Y获取四位数年份
# %m获取月份
# %d获取天数
# %H获取24小时制小时
# %I获取12小时制小时
# %M获取分钟数
# %S获取秒数
# print(time.strftime("%Y-%m-%d %I:%M:%S"))
# print(time.strftime("%y/%m/%d %H-%M-%S"))


# 获取某年某月日历
# print(calendar.month(2020, 8))

# 获取某年日历
# print(calendar.calendar(2020))
