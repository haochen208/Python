# 请输入一个成绩：如果成绩大于等于90分，输出优秀；如果大于等于70分，输出良好；如果大于等于60分，输出及格，否则输出不及格。

while True:
    score = int(input("请输入一个成绩【输入0就可以退出】："))
    if score == 0:
        break
    elif score >= 90:
        print("优秀")
    elif score >= 70:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")
