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
#
# name=[]
# while True:
#     n=input("姓名：")
#     if n=="Q":
#         print(name)
#         break
#     name.append(n)

# a=1234
# while True:
#     s=input(int("请输入密码："))
#     if a==s:
#         print("密码正确")
#         break
#     else:
#         a!=s
#         print("密码错误 请重试")

