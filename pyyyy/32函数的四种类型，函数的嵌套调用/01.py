def a1():
    print("---XXX学校元旦联欢节目单---")
    print("跳舞")
    print("唱歌")
    print("小品")
a1()

def a2(a,b):
    print(a + b)
a2(5,3)

def a3():
    return "今天有3个人没来上学"
print(a3())

def a4(c,d):
    return c - d
print(a4(100,93))


def c1():
    print("一一一一一一")
c1()

def many(n):
    for i in range(n):
        c1()
many(5)

def sum(a,b,c):
    return a+b+c

def aveg(a,b,c):
    res=sum(a,b,c)/3
    return res
print(aveg(6,10,2))