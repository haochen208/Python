# try:
#     num=int(input("请输入一个整数："))
#     print(10/num)
# except Exception as e:
#     print(e)
# else:
#     print("微笑(ﾟ▽ﾟ*) ")

# try:
#     num=int(input("请输入一个整数："))
#     print(10/num)
# except Exception as e:
#     print(e)
# else:
#     print("微笑(ﾟ▽ﾟ*) ")
# finally:
#     print("哭脸(；′⌒`)")


try:
    s  = input("请输入您的手机号：")
    if not s .startswith("1"):
        raise ValueError("您的手机号输入有误！")
except ValueError as e:
    print(e)
else:
    print(s)