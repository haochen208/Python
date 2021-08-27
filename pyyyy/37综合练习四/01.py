L=["a","b","c","c","b","a"]
# # 方法一：
print(list(set(L)))
# # 方法二：
l=[]
for i in L:
    if i not in l:
        l.append(i)
print(l)
# # 方法三：
l=[]
[l.append(i) for i in L if i not in l]
print(l)