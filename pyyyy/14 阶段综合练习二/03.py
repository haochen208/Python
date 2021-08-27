# 判断100以内有多少个质数，并输出所有质数。
# 质数：大于1，且只能被1和它自身整除的数；
# 合数：大于1，除了被1和它自身整除外，还能被其他数整除；

count = 0
for i in range(1,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print("%d是一个质数" % i)
        count += 1

print("我们一共有%d个质数" % count)



