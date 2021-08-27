# 打印如下星星：
# *
# **
# * *
# *  *
# *****

for hang in range(1,6):
    for lie in range(1,hang+1):
        if hang == 5:
            print("*",end="")
        elif lie == 1 or lie == hang:
            print("*",end="")
        else:
            print(" ",end="")
    print()

