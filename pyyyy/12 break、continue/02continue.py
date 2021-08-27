# continue：控制程序结束本次循环，直接进入下一轮循环！

# i = 1
# while i < 8:
#     i += 1
#     if i == 5:
#         continue
#     print(i)


for i in range(5):
    if i == 3:
        continue
    print(i)
