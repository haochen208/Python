# 编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组，元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有数。
def cacluate(*s):
    a = sum(s) / len(s)
    u=[]
    for i in s:
        if i > a:
            u.append(i)
    return a, u

print(cacluate(1, 2, 3, 4, 5))