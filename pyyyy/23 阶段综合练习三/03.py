# 设计一个通讯录管理系统实现如下功能：
# =====================
# 1.增加姓名和手机号
# 2.删除用户
# 3.修改手机号
# 4.查询所有用户
# 5.根据姓名查找手机号
# 6.退出系统
# =====================


# 创建一个姓名列表
names = []
# 创建一个手机号列表
telephones = []

while True:
    choice = input("""=====================
    1.增加姓名和手机号
    2.删除用户
    3.修改手机号
    4.查询所有用户
    5.根据姓名查找手机号
    6.退出系统
=====================
    请选择：""")
    if choice == "1":
        name1 = input("请输入姓名：")
        if name1.isspace() or not name1:
            print("不能输入空名字！")
        else:
            if name1 in names:
                print("该联系人已存在，请重新输入！")
                continue
            else:
                names.append(name1)
                number1 = input("请输入手机号：")
                if number1.isspace() or not number1:
                    print("不能输入空手机号！")
                else:
                    telephones.append(number1)
                    print("输入完成，该联系人存储成功！")

    elif choice == "2":
        name2 = input("请输入您要删除的联系人：")
        a = names.index(name2)
        del names[a]
        del telephones[a]
        print("删除完成，该联系人已经移除！")

    elif choice == "3":
        name3 = input("请输入要修改的联系人：")
        b = names.index(name3)
        telephones[b] = input("请输入新的手机号：")
        print("修改完成，该联系人手机号已经更换成功！")

    elif choice == "4":
        for i in range(len(names)):
            print("所有用户为：%s，%s" % (names[i], telephones[i]))
        print("查询完成，所有用户已经显示完毕！")

    elif choice == "5":
        name4 = input("请输入您要查找的联系人：")
        c = names.index(name4)
        print("您要查找的手机号为：%s" % telephones[c])

    elif choice == "6":
        print("感谢使用本系统！")
        break

    else:
        print("输入有误，请重新输入！")
