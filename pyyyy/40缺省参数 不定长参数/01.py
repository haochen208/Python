def a(e,d,f=500):
    print("商场有%d台个冰箱" %e)
    print("商场有%d个电视" %d)
    print("商场有%d个电脑" %f)
print(a(300,500,900))

def z(n,y,m=8):
    if m==8:
        return n*y*m
    else:
        return n**y
print(z(2,6))
print(z(5,2,3))