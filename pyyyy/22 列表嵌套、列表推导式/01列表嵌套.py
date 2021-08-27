# 列表嵌套：列表里面嵌列表、元组、字典、集合等

# citys = [["大连", "辽阳"], ["哈尔滨", "鹤岗"], ["长春", "吉林"]]
# print(citys[1][1])

# nums = [[1, 2], [3, 4, [5, 6, [7, 8, 9]], 10]]
# print(nums[1][2][2][1])

import random

# 定义一个大列表保存三个星球
star_list = [[], [], []]
# 定义一个列表存8位宇航员的名字
names = ["A", "B", "C", "D", "E", "F", "G", "H"]
# 开始随机分配
for name in names:
    index = random.randint(0, 2)
    star_list[index].append(name)

# 遍历分配结果
i = 1
for star in star_list:
    print("星球%d中有%d位宇航员，分别是：" % (i, len(star)))
    i += 1
    for name in star:
        print("%s" % name)
