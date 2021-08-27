names = ['jiu', 'lin', 'liang', 2, 'kun', 2, 'ting', 2]
a = names.index(2)
names_1 = names[a + 1:]
b = names_1.index(2)
print("2的索引位置为：", a + b + 1)
