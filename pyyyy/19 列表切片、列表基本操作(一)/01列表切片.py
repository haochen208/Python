mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(mylist[0:4])
# print(mylist[::])
# print(mylist[0:7:2])
# print(mylist[-1:-7:-2])
# print(mylist[::-1])
# print(mylist[9:10]) # 列表的切片索引超出最大下标不会报错，只是返回一个空列表
# print(mylist[-8:-2:-2]) # 取值方向跟步长方向不一致，取不到值


# 列表的脚本操作符：
l1 = ["a", "b", "c", "d", "e"]
l2 = [1, 2, 3, 4, 5]
l3 = ["!", "@", "#", "$"]
# 拼接（+）
# print(l1 + l2 + l3)
# 复制（*）
# print(l1 * 3)
# len()统计列表长度
# print(len(l1 * 3))
# in、not in判断元素是否在/不在列表中
# print("c" in l2)
# print(3 not in l1)