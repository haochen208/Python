# 请将列表中所有的字符串变为小写
L = ["Hello", "World", "Apple", "Banana"]

L1 = []
for i in L:
    L1.append(i.lower())
print(L1)

# 列表推导式：[表达式 for 变量 in 序列]
print([i.lower() for i in L])
