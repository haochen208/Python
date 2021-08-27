# 对列表list = [23,13,2,35,12,1,10]中的每一个元素加1，并排序。

list = [23,13,2,35,12,1,10]
list_new = []
for i in list:
    i += 1
    list_new.append(i)

# print(sorted(list_new))
list_new.sort()
print(list_new)