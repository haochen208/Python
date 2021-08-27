# 输入两个字符串，从第一个字符串中删除第二个字符串中所有的字符。
# 例如：输入"They are students."和"aeiou"，删除之后第一个字符串变为"Thy r stdnts."

str1 = input("请输入第一个字符串：")
str2 = input("请输入第二个字符串：")
str3 = ""

for i in str1:
    if i not in str2:
        str3 += i
print(str3)