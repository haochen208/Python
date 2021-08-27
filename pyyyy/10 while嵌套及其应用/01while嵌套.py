# while 条件1：
#     满足条件1执行的语句
#     while 条件2：
#         满足条件2执行的循环

# ★☆
# 打印10行10列星星
# ★★★★★★★★★★
# ★★★★★★★★★★
# ★★★★★★★★★★
# ★★★★★★★★★★
# ★★★★★★★★★★
# ★★★★★★★★★★
# ★★★★★★★★★★
# ★★★★★★★★★★
# ★★★★★★★★★★
# ★★★★★★★★★★
# hang = 0
# while hang < 10:
#     lie = 0
#     while lie < 10:
#         print("★", end="")
#         lie += 1
#     print()
#     hang += 1

# 打印10行10列隔行变色星星
# ★★★★★★★★★★
# ☆☆☆☆☆☆☆☆☆☆
# ★★★★★★★★★★
# ☆☆☆☆☆☆☆☆☆☆
# ★★★★★★★★★★
# ☆☆☆☆☆☆☆☆☆☆
# ★★★★★★★★★★
# ☆☆☆☆☆☆☆☆☆☆
# ★★★★★★★★★★
# ☆☆☆☆☆☆☆☆☆☆
# hang = 1
# while hang < 11:
#     lie = 0
#     while lie < 10:
#         if hang % 2 == 1:
#             print("★", end="")
#         else:
#             print("☆", end="")
#         lie += 1
#     print()
#     hang += 1

# 打印如下图像
# *
# **
# ***
# ****
# *****
hang = 1
while hang < 10:
    lie = 1
    while lie <= hang:
        print("%d*%d=%-4d" % (lie,hang,lie*hang),end="")
        lie += 1
    print()
    hang += 1

# hang = 1
# while hang < 6:
#     lie = 1
#     while lie <= hang:
#         print("*",end="")
#         lie += 1
#     print()
#     hang += 1



