# 对第4题升级：支持用户持续输入，若输入Q或q退出，性别默认为男，如果遇到女学生，则把性别输入女。
def func(name,age,edu,gender='男'):
    f = open('student_msg',mode='a',encoding='utf-8')
    f.write(name+'_'+gender+'_'+age+'_'+edu+'\n')
    f.flush()
    f.close()
while 1:
    NAME=input("请输入你的名字:")
    GENDER=input("请输入你的性别:")
    AGE=input("请输入你的年龄:")
    EDU=input("请输入你的学历:")
    if GENDER == '':
        func(NAME,AGE,EDU)
    else:
        func(NAME,AGE,EDU,GENDER)
    content = input("录入完毕,是否还要继续输入(输入q就退出):")
    if content.upper() == 'Q':
        break
