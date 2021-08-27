# 字典也是可变类型！

info = {"name": "昊宸", "age": 12, "sex": "男"}
# 修改元素：给已经存在的键进行重新赋值----->字典名["键名"] = 新的值
# info["age"] = 13
# print(info)

# 增加元素：给不存在的键进行赋值------>字典名["键名"] = 新的值
# info["school"] = "清华大学"
# print(info)

# 删除元素：删除指定键值对----->del 字典名["键名"]
#         删除整个字典------->del 字典名
#         清空字典---------->字典名.clear()
# del info["sex"]
# print(info)

# del info
# print(info)

# info.clear()
# print(info)

# 查找元素：根据键查找指定值------->字典名["键名"]
# print(info["name"])




# 将列表中的字符串"1"变成数字101
li = [["k", ["qwe", 20, {"k1": ["tt", 3, "1"]}, 89], "ab"]]
