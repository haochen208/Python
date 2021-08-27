# 用程序实现用户登录的功能，输入用户名和密码都正确则登录成功，否则登录失败，有三次尝试机会。

name = "geekstar"
password = "123456"
i = 1
while i <= 3:
    Ming = input("请输入您的用户名：")
    MiMa = input("请输入您的密码：")
    if Ming == name and MiMa == password:
        print("恭喜你登录成功！")
        break
    else:
        print("您还剩下%d次机会" % (3 - i))
        if (3 - i) == 0:
            print("不好意思今天次数已用完，明天再登录！")
            break
    i += 1
