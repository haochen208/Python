# 判断闰年？
# （1）年份能被4整除并且不能被100整除；
# （2）能被400整除。

year = int(input("请输入一个年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("%d是闰年" % year)
else:
    print("%d不是闰年" % year)
