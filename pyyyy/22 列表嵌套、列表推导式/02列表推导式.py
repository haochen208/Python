# 三元表达式：为真的结果 if 条件 else 为假的结果

# 列表推导式：
# 应用一：[表达式  for 变量 in 序列]
# 应用二：[表达式  for 变量 in 序列 if 条件 ]
# 应用三：[满足条件的表达式  if 条件 else 不满足条件的表达式  for 变量 in 序列]

# 创建一个由平方数组成的列表[0,1,4,9,16,25,36,49,64,81]
# 应用一：
# squares = []
# for i in range(10):
#     squares.append(i ** 2)
# print(squares)
#
# print([i ** 2 for i in range(10)])

# 应用二：
# squares = []
# for i in range(10):
#     if i % 2 == 0:
#         squares.append(i ** 2)
# print(squares)
#
# print([i ** 2 for i in range(10) if i % 2 == 0])

# 应用三：
# squares = []
# for i in range(10):
#     if i % 2 == 0:
#         squares.append(i ** 2)
#     else:
#         squares.append(i ** 3)
# print(squares)
#
# print([i ** 2 if i % 2 == 0 else i ** 3 for i in range(10)])
