# range(起点，终点，步长)
# 默认终点取不到

# 默认写法
# for i in range(1,5,1):
#     print(i)

# 步长为1，默认不写
# for j in range(2,6):
#     print(j)

# 起点为0，起点可以不写
# for k in range(6):
#     print(k)

# 步长为负，从右往左取值
# for l in range(5,1,-2):
#     print(l)

# str = "hello python"找出下标对应元素
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o
# 5
# 6 p
# 7 y
# 8 t
# 9 h
# 10 o
# 11 n
str = "hello python"
for i in range(len(str)):
    print(i,str[i])

# print(str[0])
# print(str[1])
# 。。。。。。
# print(str[11])




