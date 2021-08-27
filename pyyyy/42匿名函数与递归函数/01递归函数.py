# 函数嵌套：在一个函数里面调用别的函数。
# 递归函数：在一个函数里面调用自己。

# 递归的好处：
# （1）简洁优雅
# （2）将复杂问题简单化
# （3）比嵌套循环写法更容易


# 计算一个数的阶乘？
# n! = n * n-1 * n-2 * ... * 1

# 1! = 1
# 2! = 2 * 1
# 3! = 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1
# ......
# n! = n * (n-1)!  【n > 1】


# 循环写法：
# def JieCheng(n):
#     Ji = 1
#     for i in range(n, 0, -1):
#         Ji *= i
#     return Ji
#
# print(JieCheng(5))

# 递归写法：
# def JieCheng(n):
#     if n > 1:
#         res = n * JieCheng(n - 1)
#     else:
#         res = 1
#     return res
#
# print(JieCheng(4))


# 计算n的m次方？
# n^m = n * n^(m-1)  【m > 1】

# def power(n, m):
#     if m == 1:
#         return n
#     else:
#         return n * power(n, m - 1)
#
# print(power(2, 3))


