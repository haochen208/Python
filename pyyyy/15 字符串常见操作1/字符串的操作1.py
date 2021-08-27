str = "hello python hello world"
str1 = "hellopython"
str2 = "123456789"
str3 = "hello520"
str4 = "\n"

# find()【查找】搜索字符串中是否包含某个子串，如果包含返回索引，否则返回-1，可以指定查找的开始和结尾。
# print(str.find("y",8,14))

# rfind()【查找】从右边开始查找
# print(str.rfind("l"))

# index()【查找】跟find()差不多，查到返回索引，查不到报错。
# print(str.index("y",8,14))

# rindex()【查找】从右边开始查找
# print(str.rindex("l"))

# count()【数量】在开始和结尾之间，查找某个子串出现的次数
# print(str.count("ll"))
# print(str.count("y"))
# print(str.count("o",4,18))

# replace()【替换】把字符串中的某个子串1替换成某个子串2，可以指定替换的次数
# print(str.replace("o", "O", 2))

# split()【分割】可以把字符串以某个分隔符进行分割，可以指定最大分割次数
# print(str.split(" ",1))

# isalpha()【判断字母】判断字符串中是否全部是字母，如果都是返回真，否则返回假
# print(str1.isalpha())

# isdigit()【判断数字】判断字符串中是否全部是数字，如果都是返回真，否则返回假
# print(str2.isdigit())

# isalnum()【判断字母或数字】判断字符串中是否全部是数字或字母，如果都是返回真，否则返回假
# print(str3.isalnum())

# isspace()【判断空白】判断字符串中是否全部是空白，如果都是返回真，否则返回假
# print(str4.isspace())


# 输入一段字符，分别统计出其中的英文字母、空格、数字、和其他字符的个数？
str = input("请输入一段字符：")
alpha = 0
digit = 0
space = 0
others = 0
for s in str:
    if s.isalpha():
        alpha += 1
    elif s.isdigit():
        digit += 1
    elif s.isspace():
        space += 1
    else:
        others += 1
print("您的这段字符里面有%d个字母，%d个数字，%d个空格，%d个其他字符" % (alpha, digit, space, others))
