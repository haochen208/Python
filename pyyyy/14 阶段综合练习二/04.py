# 计算给定数字的阶乘
# 阶乘：8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40320

n = int(input("请输入一个数："))
JI = 1
for i in range(n,0,-1):
    JI *= i

print(JI)