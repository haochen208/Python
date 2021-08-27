str1 = "hello python hello world"
str2 = "HELLO PYTHON HELLO WORLD"
str3 = "hello"
str4 = "      hello"
str5 = "hello      "
str6 = "   hello   "
str7 = ","

# capitalize()【第一个首字母大写】把字符串第一个首字母大写
# print(str1.capitalize())

# title()【所有首字母大写】把字符串每个单词首字母都大写
# print(str1.title())

# startswith()【检查开头】检查字符串是否以指定字符开头
# print(str1.startswith("hello"))

# endswith()【检查结尾】检查是否以指定字符结尾
# print(str1.endswith("world"))

# lower()【大写变小写】将字符串中的所有大写字符变为小写
# print(str2.lower())

# upper()【小写变大写】将字符串中的所有小写字符变为大写
# print(str1.upper())

# ljust()【左对齐】将字符串左对齐，并使用空格填充至你指定的长度
# print(str3.ljust(10))

# rjust()【右对齐】将字符串右对齐，并使用空格填充至你指定的长度
# print(str3.rjust(10))

# center()【居中对齐】将字符串居中对齐，并使用空格填充至你指定的长度
# print(str3.center(10))

# lstrip()【删除左空白】删除字符串左边的空白
# print(str4.lstrip())

# rstrip()【删除右空白】删除字符串右边的空白
# print(str5.rstrip())

# strip()【删除两端空白】删除字符串两端的空白
# print(str6.strip())

# join()【拼接】拼接字符串
# print(str7.join(str1))


# 判断变量名命名是否合法？【数字、字母、下划线组成，其中数字不能开头】
var = input("请输入一个变量名：").strip()
# 判断第一个字母是否合法？
if var[0] == "_" or var[0].isalpha():
    # 判断除了第一个字符之外其他字符是否合法？
    for char in var[1:]:
        if not (char.isalnum() or char == "_"):
            print("变量名%s不合法" % var)
            break
    else:
        print("变量名%s合法" % var)

else:
    print("变量名不合法，首字符有问题！")
