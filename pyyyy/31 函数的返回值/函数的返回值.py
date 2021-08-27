# 返回值：函数在执行完成之后返回给调用者的结果。

# def add(a, b):
#     return a + b

# print(add(3, 4))
# res = add(4, 5)
# print(res)


# return的用法：
# （1）返回值：将一个或多个值进行返回，可以返回常量、变量、表达式等等。
# name = "吕昊宸"
# def info(a, b):
#     return 520
#     return "你好啊"
#     return name
#     return a + b
#     return "哈哈哈哈" if a > b else "啊啊啊啊"
#     return a, b
#
# print(info(1, 2))

# （2）终止函数，一旦执行return函数立马终止，不再执行后面的任何代码了。
# def info():
#     print("---1---")
#     return "欢迎光临"
#     print("---2---")
#
# print(info())

# def info(a, b):
#     print("欢迎光临")
#     if a > b:
#         return "哈哈哈哈"
#     else:
#         return "啊啊啊啊"
#     print("下次再来")
#
#
# print(info(20, 5))
