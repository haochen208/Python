# 删除namelist列表中与removelist列表相同的元素。
namelist = ['stu1', 'stu2', 'stu3', 'stu4', 'stu5', 'stu6', 'stu7']
removelist = ['stu1', 'stu3', 'stu5', 'stu6']

for i in namelist:
    if i in removelist:
        namelist.remove(i)

print(namelist)
