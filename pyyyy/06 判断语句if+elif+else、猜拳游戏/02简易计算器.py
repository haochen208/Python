num1 = int(input("请输入第一个数字："))
fh = input("请输入运算符号：")
num2 = int(input("请输入第二个数字："))
if fh == "+":
    print(num1 + num2)
elif fh == "-":
    print(num1 - num2)
elif fh == "*":
    print(num1 * num2)
elif fh == "/":
    print(num1 / num2)
else:
    print("我们只能进行加减乘除运算，请输入正确符号！")
