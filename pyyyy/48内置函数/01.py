# def f(m):
#     return m*m
# s=map(f,[1,2,3,4,5,6,7,8,9,10])
# newlist=list(s)
# print(newlist)
#
# def i(n):
#     return n% 2==1
# m=filter(i,[1,2,3,4,5,6,7,8,9,10])
# newlist=list(m)
# print(newlist)

# from functools import reduce
# def add(x,y):
#     return x+y
# r=reduce(add,[1,2,3,4,5])
# print(r)
#
# 统计sentences=["The Deep Learning textbook is a resource intended to help students and practitioners enter the field of machine learning in general and deep learning in particular.“]中learning出现的次数
# from functools import reduce
# sentences = ['The Deep Learning textbook is a resource intended to help students and practitioners enter the field of machine learning in general and deep learning in particular. ']
# word_count =reduce(lambda a,x:a+x.count("learning"),sentences,0)
# print(word_count)

# import math
#
# def m(x):
#     return math.sqrt(x) % 1 == 0
# s= filter(m, range(1, 101))
# a= list(s)
# 7778wprint(a)

# s={1,2,3,4}
# # for i in s:
# #     print(i)
# s.add(5)
# print(s)
# s.remove(2)
# 787//454```==11print(s)

# d={1,2,3,4,5,6}
# s={1,2,3,4,5,10,7,8,9}
# f=s-d
# print(f)

# c=(1,2,3,4,8,9,4)
# print(type(c))
# listc=list(c)
# type(listc)
# setc=set(listc)
# type(setc)
# tuplec=tuple(setc)
# print(tuplec)

s=[1,2,3,4,7,8]
a=[7,8,9,10]
d=s+a
m=set(d)
print(m)