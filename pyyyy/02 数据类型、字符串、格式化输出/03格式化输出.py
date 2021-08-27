# name1 = "吕昊宸"
# name2 = "胡歌"
# print("我的名字是:name1")

# (1)%格式化输出
# %d格式化输出整数
# num1 = 620
# print("今天的日期是：%d" % num1)

# %f格式化输出小数，默认保留6位小数，超过6位四舍五入，不够6位拿0补全6位，可以指定保留的位数
# num2 = 3.1415926
# print("圆周率是：%.2f" % num2)

# %s格式化输出字符串
s = 'abcdefg'
print("有一些英文字字母为：%s" % s)


# (2)format格式化输出
# s1 = "hello"
# s2 = "python"
# print("{} {}".format(s1, s2))   # 默认按顺序
# print("{1} {0}".format(s1, s2)) # 设置指定位置
# print("{0}，{1}，{0}".format(s1, s2))
# print("我的名字是:{}".format("吕昊宸"))