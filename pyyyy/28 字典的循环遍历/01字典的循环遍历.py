# for ... in ...可以对字符串、列表、元组、字典、range()进行遍历

info = {"name": "昊宸", "age": 12, "sex": "男"}
# （1）对字典直接遍历，会遍历所有的键
# for i in info:
#     print(i)

# （2）keys()指定遍历所有的键
# for i in info.keys():
#     print(i)

# （3）values()指定遍历所有的值
# for i in info.values():
#     print(i)

# （4）items()指定遍历(键,值)元组
# for i in info.items():
#     print(i)

# （5）遍历所有的键值对
# for i, j in info.items():
#     print(i, j)

# 想一想，如何实现带下标索引的遍历？
l = ["a", "b", "c", "d"]
# 0 a
# 1 b
# 2 c
# 3 d
# j = 0
# for i in l:
#     print(j, i)
#     j += 1

# enumerate()可以将可遍历的数据组合成一个索引序列，一个是索引，另一个是数据。
# for j, i in enumerate(l):
#     print(j, i)

# for j,i in enumerate(info.items()):
#     print(j,i)
