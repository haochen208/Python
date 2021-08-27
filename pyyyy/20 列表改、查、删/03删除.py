# 删除元素（del、remove、pop）

names = ["赵二", "张三", "李四", "王五", "张三"]
# （1）del 根据下标索引来删除元素
# del names[1]
# print(names)

# del names
# print(names)

# （2）remove() 根据元素的值来删除
# names.remove("张三")
# print(names)

# （3）pop() 不写索引默认删除最后一个元素，并返回；带索引的话删除指定元素，并返回
# print(names.pop())
# print(names)

# print(names.pop(2))
# print(names)