# 任意输入一串字符，输出其中不同字符以及各自的个数。

str = input("请输入字符串:")
dict = {}
for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

