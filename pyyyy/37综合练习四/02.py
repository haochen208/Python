# 将所有大于66的值保存到字典的一个键中，将小于66的值保存到第二个键中。
# {"k1":大于66的所有值列表, "k2":小于66的所有值列表}
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 101]
a={}
k1=[]
k2=[]
for i in l:
    if i > 66:
        k1.append(i)
    elif i < 66:
        k2.append(i)
a["k1"]=k1
a["k2"]=k2
print(a)
