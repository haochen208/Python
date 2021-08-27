### 定义主界面函数
def home_page():
    print("""====================欢迎使用XX银行ATM自助存取款系统========================
                             1：登陆账号
                             2：注册账号
                             3：退出系统
====================欢迎使用XX银行ATM自助存取款系统========================""")

# home_page()

### 用列表存储多个用户的信息，每个用户信息存在字典中
Account = [{"Name": "张三", "Password": "123456", "Money": 10000},
           {"Name": "李四", "Password": "654321", "Money": 20000}]

### 单独用来存储用户名和密码的列表
name_list = []
password_list = []


### 定义一个用户遍历函数（提取出来Account里面所有的用户名和密码）
def name_password():
    for i in Account:
        name_list.append(i["Name"])
        password_list.append(i["Password"])


### 登陆函数
def user_login():
    name_password()
    MingZhi = input("请输入您的用户名：")
    MiMa = input("请输入您的6位数密码：")
    if MingZhi in name_list:
        for i in Account:
            if MingZhi == i["Name"] and MiMa == i["Password"]:
                print("尊贵的%s用户您好，您的余额为%d元" % (i["Name"], i["Money"]))
                break
        else:
            print("密码错误，请重新输入！")
    else:
        print("该用户名未注册！")

# user_login()

### 注册函数
def new_account():
    name_password()
    ### 注册用户名
    while True:
        MingZhi = input("请输入您的用户名：")
        if MingZhi in name_list:
            print("该用户名已经注册过，请重新输入！")
        elif " " in MingZhi:
            print("用户名中不能含有空白，请重新输入！")
        else:
            new_user = {"Name":MingZhi}
            Account.append(new_user)
            break

    ### 注册密码
    while True:
        MiMa1 = input("请输入您的6位数纯数字密码：")
        MiMa2 = input("请再次输入您的6位数纯数字密码：")
        if MiMa1 != MiMa2:
            print("两次密码输入不一致，请重新输入！")
        else:
            if not MiMa2.isdigit():
                print("密码不是纯数字请重新输入！")
            elif len(MiMa2) != 6:
                print("密码长度不正确请重新输入！")
            else:
                new_user["Password"] = MiMa2
                print("恭喜你，新账户注册成功！")
                break

# new_account()

    select=input("是否要预存金额（是：按“0”然后回车；否：直接回车）：")
    if select =="0":
        money=int(input("请输入您的预存款金额："))
        new_user["Money"]=money
        print("预存款成功，存款金额为%d元" % money)

def main():
    while True:
        home_page()
        choice=input("请输入您需要的服务：")
        if choice=="1":
            user_login()
        elif choice=="2":
            new_account()
        elif choice=="3":
            print("感谢您的使用！")
            break
        else:
            print("您的操作无效，请重新输入！")
main()