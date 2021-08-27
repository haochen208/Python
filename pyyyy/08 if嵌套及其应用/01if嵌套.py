# num = int(input("请输入一个数字："))
# if num > 0:
#     if num > 100:
#         print("这个数字大于100")
#     else:
#         print("这个数字在0-100之间")
# else:
#     print("这个数字为负数")



# Piao = 1  # 用1代表有票，0代表没票
# Dao = 19  # 数字代表刀子的长度
#
# if Dao < 10:
#     print('我们通过安检了')
#     if Piao == 1:
#         print("我们有票，可以上车了")
#     else:
#         print("我们没票，请补票")
# else:
#     print("我们没有通过安检")



money = 88  # 数字代表金额
zuoWei = 0  # 0代表没座位，1代表有座位
if money >= 2:
    print("我们可以上车")
    if zuoWei == 1:
        print("有座位，我们可以坐下！")
    else:
        print("没座位，只能站着！")
else:
    print("钱不够不能上车！")


