# 水仙花数
# 水仙花数是一个三位数，每位上的数字立方和等于该数本身
# 百位的3次方 + 十位的3次方 + 个位的3次方 = 这个数
# 1**3 + 5**3 + 3**3 = 153

for i in range(100, 1000):
    B = i // 100
    S = (i - B * 100) // 10
    G = i % 10
    sum = B ** 3 + S ** 3 + G ** 3
    if sum == i:
        print("%d是水仙花数" % i)

