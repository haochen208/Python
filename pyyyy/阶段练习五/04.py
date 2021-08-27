# 写函数，函数接收4个参数，分别是：姓名，性别，年龄，学历
# 用户通过输入这4个内容，然后将这4个内容传入到函数中，此函数接收到这4个参数后，将内容追加到一个student_msg文件中。
def student(s,a,h,z):
    s=input("请输入你的名字：")
    a=input("请输入你的性别：")
    h=input("请输入你的年龄：")
    z=input("请输入你的学历：")
student("小明","男",13,"初中")
f=open("student_msg","w",encoding="UTF-8")


