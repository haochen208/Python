# names = ["小明", "小红", "小张", "小朱", "小王"]
# print(names.index("小明"))  # 可能很快
# print(names.index("小王"))  # 可能很慢


# 字典dict：多数据类型，查询速度很快。
# key------>键
# value---->值
# d = {key1: value1, key2: value2, key3: value3...}

# info = {"name": "昊宸", "age": 12, "sex": "男"}
# 通过键访问值：字典名[键名]
# print(info["sex"])

# 访问不存在的键，会报错
# print(info["school"])

# get()访问不存在的键，会返回None；存在，返回键对应的值。
# print(info.get("school"))
# print(info.get("name"))

# get()可以写默认值，访问的键不存在，返回默认值；存在，返回键对应的值。
# print(info.get("school", "清华大学"))
# print(info.get("age", 13))

# 练习：
# dict1 = {"k1": "v1", "k2": "v2", "k3": "v3", "k4": "v4"}
# （1）获取字典中k2对应的值
# （2）获取字典中k6对应的值，如果不存在，则不报错，并且让他返回v6