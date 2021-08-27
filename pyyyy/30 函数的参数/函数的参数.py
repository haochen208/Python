# def add():
#     a = 2
#     b = 3
#     print(a + b)
#
# add()

# 参数：在函数内部中不确定的数据拿参数先占位置。

# def add(a, b):
#     print(a + b)
#
# add(7, 8)

# 形参（a, b）：定义函数时小括号里面的参数，用来接收值的。
# 实参（7, 8）：调用函数时小括号里面的参数，用来赋值的。


# 输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符。
# 例如：输入"They are students."和"aeiou"，删除之后第一个字符串变为"Thy r stdnts."

# def String(str1, str2):
#     """输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符"""
#     str3 = ""
#     for i in str1:
#         if i not in str2:
#             str3 += i
#     print(str3)
#
# s1 = input("请输入第一个字符串：")
# s2 = input("请输入第二个字符串：")
# String(s1, s2)


# 请将列表中所有的字符串变为小写
# def low(L):
#     L1 = []
#     for i in L:
#         L1.append(i.lower())
#     print(L1)
#
# L = ["Hello", "World", "Apple", "Banana"]
# low(L)


# 写函数，计算传入字符串中的【数字】、【字母】、【空格】和【其他】的个数。
def func(p):
   digit_number = 0
   space_number = 0
   alpha_number = 0
   else_number = 0
   for i in p:
      if i.isdigit():    # 检查字符串是否只由数字组成
         digit_number += 1
      elif i.isspace():  # 检查字符串是否只由空格组成
         space_number += 1
      elif i.isalpha():  # 检查字符串是否只由字母组成
         alpha_number += 1
      else:
         else_number += 1
   print(digit_number, space_number, alpha_number, else_number)

func("hell  o#$")  # 调用检验

