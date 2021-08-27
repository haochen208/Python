# if 条件1：
#     执行语句1
# elif 条件2：
#     执行语句2
# elif 条件3：
#     执行语句3
# ......
# else:
#     最后的执行语句

score = int(input("请输入您的成绩："))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")