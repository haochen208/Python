# 匿名函数：省略了函数的声明步骤，就是没有函数名，里面不能写return，整个函数的运行结果就是返回值，所以需要定义变量来保存结果。

# 语法格式：lambda 参数:方法


# 求两数之和？
# def add(a, b):
#     return a + b
# print(add(1, 2))

# add = lambda a, b: a + b
# print(add(1, 2))

# 注意：（1）匿名函数可以接收任意数量的参数，但是只能返回一个表达式的值。
#      （2）匿名函数里面不要直接print，最好将结果返回出来。


# # 指定按name排序还是age排序？
# stu = [{"name": "zhangsan", "age": 18}, {"name": "lisi", "age": 19}, {"name": "wangwu", "age": 17}]
#
# # 按name排序
# print(sorted(stu, key=lambda x: x["name"]))
# # 按age排序，并且倒序
# print(sorted(stu, key=lambda x: x["age"], reverse=True))


# 匿名函数支持三元表达式
# lambda 参数:方法1 if 条件 else 方法2

# f = lambda x, y: x + y if x > y else x * y
# print(f(3, 2))
# print(f(2, 3))

x=2
y=4
print(x*y)