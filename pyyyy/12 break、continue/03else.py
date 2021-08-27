# else：循环没有中途退出【没有执行break】，循环结束后就可以执行else里面的代码！

# for i in "好好学习天天向上":
#     if i == "天":
#         break
#     print(i)
# else:
#     print("for循环结束了！")

# 注意：
# （1）break和continue只能用在循环里面，除此之外不能单独使用！
# （2）一个break或一个continue只能终止一个循环，如果是嵌套循环，只对最近的一层循环起作用！

# for hang in range(1,10):
#     if hang == 5:
#         break
#     for lie in range(1,hang+1):
#         if lie == 5:
#             break
#         print("%d*%d=%-4d" % (lie,hang,lie*hang),end="")
#     print()

# 求1-100不是7的倍数的和？
sum = 0
for i in range(1,101):
    if i % 7 == 0:
        continue
    sum += i
print(sum)

