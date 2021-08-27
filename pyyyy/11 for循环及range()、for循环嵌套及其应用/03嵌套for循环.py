# for hang in range(9):
#     for lie in range(hang+1):
#         print("*",end="")
#     print()

# for hang in range(1,10):
#     for lie in range(1,hang+1):
#         print("%d*%d=%-4d" % (lie,hang,lie*hang),end="")
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *

# 第一种写法：
# for hang in range(1,6):
#     for lie in range(1,hang+1):
#         print("* ",end="")
#     print()

# 第二种写法：
for i in range(1,6):
    print("* " * i)