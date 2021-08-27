### 定义一个列表用来存储所有学生信息（每个学生是一个字典）
info_list = []


### 主界面函数
def menu():
    print("------------------------")
    print("     学生管理系统V1.0      ")
    print("       1：添加学生        ")
    print("       2：移除学生        ")
    print("       3：修改学生        ")
    print("       4：查找学生        ")
    print("       5：显示所有学生     ")
    print("       6：退出系统        ")
    print("------------------------")


### menu()

### 添加学生信息
def add_new_info():
    new_name = input("请输入姓名：")
    new_tel = input("请输入手机号：")
    new_qq = input("请输入QQ号：")

    for temp in info_list:
        if new_name == temp["name"]:
            print("该学生已经存在，请不要重复添加信息！")
            return

    ### 定义一个字典用来存储学生的三个信息
    info = {}
    info["name"] = new_name
    info["tel"] = new_tel
    info["qq"] = new_qq
    ### 向列表中添加这个字典
    info_list.append(info)


### add_new_info()
### print(info_list)


### 删除学生
def del_info():
    del_num = int(input("请输入要删除的学生序号："))
    if len(info_list) > del_num >= 0:
        del_flag = input("您真的要删除吗【yes or no】？")
        if del_flag == "yes":
            del info_list[del_num]
    else:
        print("您输入的序号找不到此学生，请重新输入！")


### del_info()
### print(info_list)


### 修改学生
def modify_info():
    modify_num = int(input("请输入要修改的学生序号："))
    if len(info_list) > modify_num >= 0:
        print("您要修改的学生信息目前如下：")
        print("姓名：%s，手机号：%s，QQ号：%s" % (
            info_list[modify_num]["name"], info_list[modify_num]["tel"], info_list[modify_num]["qq"]))
        info_list[modify_num]["name"] = input("请输入新的姓名：")
        info_list[modify_num]["tel"] = input("请输入新的手机号：")
        info_list[modify_num]["qq"] = input("请输入新的QQ号：")
    else:
        print("您输入的序号找不到此学生，请重新输入！")


### modify_info()
### print(info_list)


### 查找学生
def search_info():
    search_name = input("请输入要查询的学生姓名：")
    for temp in info_list:
        if temp["name"] == search_name:
            print("该学生的信息如下：")
            print("姓名：%s，手机号：%s，QQ号：%s" % (temp["name"], temp["tel"], temp["qq"]))
            break
    else:
        print("查无此人，请重新输入！")


### search_info()


### 显示所有学生
def print_all_info():
    i = 0
    for temp in info_list:
        print("序号：%d， 姓名：%s，手机号：%s，QQ号：%s" % (i, temp["name"], temp["tel"], temp["qq"]))
        i += 1


### print_all_info()


### 主函数
def main():
    while True:
        menu()
        num = input("请输入您要进行的操作：")
        if num == "1":
            add_new_info()
        elif num == "2":
            del_info()
        elif num == "3":
            modify_info()
        elif num == "4":
            search_info()
        elif num == "5":
            print_all_info()
        elif num == "6":
            print("感谢使用本系统！")
            break
        else:
            print("您的操作无效，请重新输入！")


main()
l1 = [11,22,33]
l2 = [22,33,44]
s1 = set(l1)
s2 = set(l2)
s = s1 & s2
print(s)