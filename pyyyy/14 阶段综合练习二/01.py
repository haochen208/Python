# 猜年龄？
# 用户最多尝试3次，每尝试3次后，如果还没猜对就问用户是否还想继续玩
# 如果回答Y，就继续再来猜3次
# 如果回答N，就退出程序
# 如果猜对了，也直接退出程序

age = 18
count = 0
while True:
    if count == 3:
        choice = input("是否还要继续【是Y】：")
        if choice.upper() == "Y":
            count = 0
        else:
            break
    guesss = int(input("请输入您要猜的年龄："))
    if guesss == age:
        print("恭喜你猜对了！")
        break
    count += 1


