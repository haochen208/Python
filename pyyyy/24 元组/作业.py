# 用1，2，3，4，5，6，7，8 ，8个数，能组成多少个互不相同且无重复的两位数？

# 语法：条件（if/elif/else）、循环（for/while）
# 数据类型：数字、字符串、列表、元组

li = []
for s in range(1, 9):
    for g in range(1, 9):
        if s != g:
            # li.append(s * 10 + g)
            # li.append("".join((str(s),str(g))))
            li.append(str(s) + str(g))
print(li)
print(len(li))
