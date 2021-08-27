import random

player = int(input("请输入您的拳法（剪刀1，石头2，布3）："))
computer = random.randint(1, 3)
if player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
    print("你赢了！")
elif player == computer:
    print("平局了!")
else:
    print("你输了！")
