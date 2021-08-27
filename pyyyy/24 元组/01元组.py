# 数字（int/float/bool）
# 字符串（str）
# 列表（list）
# 元组（tuple）


# 元组跟列表的不同点：
# （1）形式上不同：
# 列表list---->[]
# 元组tuple---->()

# （2）单个元素写法不同：
# 列表：
# l = ["a"]
# print(l)
# print(type(l))
# 元组：
# t = (12,)
# print(t)
# print(type(t))

# （3）类型不同：
# 列表：可变类型（增删改查）
# append/extend/insert/del/remove/pop/列表[索引]=值/index/count/in/not in
# 元组：不可变类型（查）
# t = ("a", "d", "f", "r", "a")
# print(t.index("f"))
# print(t.count("a"))
# print("r" in t)
# print("a" not in t)


# 元组跟列表的相同点：
# （1）拼接（+）、复制（*）
# t1 = (1, 2, 3)
# t2 = ("a", "b", "c")
# print(t1 + t2)
# print(t1 * 3)

# （2）len()查看数据长度
# t3 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 3, 2, 1, 3, 5, 6)
# print(len(t3))

# （3）索引、切片[起始:结束:步长]
# t4 = (5, 6, 7, 3, 1, 8, 0, 3, 5, 7)
# print(t4[5])
# print(t4[2:8:2])
# print(t4[:5:3])
# print(t4[:6])
# print(t4[2:])
# print(t4[3::3])
# print(t4[2:7:-1])
# print(t4[-2:-6:-2])
# print(t4[8:3:-2])
# print(t4[::-1])

# （4）循环遍历
# t5 = ("f", "r", "t", "y", "v")
# for i in t5:
#     if i == "r":
#         break
#     print(i)

# （5）类型转换
# 列表 ----> 元组
# l = [1, 3, 1, 4, 5, 2, 1]
# print(tuple(l))
# 元组 ----> 列表
# t = (3, 4, 5, 6, 1, 2, 3)
# print(list(t))


# 练习：
tu = ("alex", "eric", "Witharush")
# （1）计算元组长度并输出
# （2）获取元组第二个元素并输出
# （3）获取元组的第1-2个元素并输出
# （4）使用for循环输出元组的所有元素
# （5）使用for、len、range输出元素的索引