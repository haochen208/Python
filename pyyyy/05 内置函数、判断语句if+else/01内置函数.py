# abs() 返回数字的绝对值
# print(abs(-34))


# max() 返回给定参数的最大值
# print(max("haocen"))
# print(max("123456789"))
# print(max([1, 2, 3, 4, 5]))
# print(max(3, 5, 7, 9))


# round() 返回浮点数四舍五入的值
# print(round(3.1415926,4))


import random

# 随机小数     1>范围>=0
# print(random.random())

# 随机整数     b>=范围>=a
# print(random.randint(1, 5))

# 随机整数     b>范围>=a
# print(random.randrange(1, 10, 2))
# print(random.randrange(1, 100, 2))


# ord() 编码
# print(ord("@"))

# chr() 解码
# print(chr(64))

# eval() 执行一个字符串表达式，并返回表达式的结果
print(eval("1+1"))
# print(eval("3-1"))
# print(eval("4*7"))
# print(eval("5/2"))
# print(eval("4*7+1/3+4*4"))
#
# while True:
#     a = int(input())
#     if a % 2 == 0:
#         break
#     else:
#         print(a * 2)
# math = float(input("数学："))
# chinese = float(input("语文："))
# english = float(input("英语："))
# score = math + chinese + english
# print(score)
# if score >= 270:
#     print("优秀")
# elif score >= 240:
#     print("良好")
# elif score >= 180:
#     print("合格")
# else:
#     print("不合格")
#

# import random
#
# lis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# caipiao = random.sample(lis, 5)
# caipiao = ''.join(caipiao)
# shuru = input("输入号码：")
# if caipiao == shuru:
#     print("彩票号:" + caipiao)
#     print("奖金:10000元")
# else:
#     i = 0
#     for s in shuru:
#         if s in caipiao:
#             i += 1
#     print("彩票号:" + caipiao)
#     print("奖金:" + str(i * 1000) + "元")
# while True:
#     s=int(input("请输入密码："))
#     a=1234
#     if s == a:
#         print("密码正确")
#         break
#     else :
#         s != a
#         print("密码错误，请重新输入！")

# s = int(input("请输入感冒指数："))
# if 0 <= s <= 6:
#     print("少发")
# elif 6 < s <= 19:
#     print("较易发")
# elif 19 < s <= 30:
#     print("易发")
# elif 30 < s <= 61:
#     print("极易发")
# elif s < 0 or 61 < s:
#     print("指数不正确")

name=[]
while True:
    n=input("姓名：")
    if n=="Q":
        print(name)
        break
    name.append(n)