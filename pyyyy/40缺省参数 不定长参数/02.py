def info(*args):
    print(args)
info(1)
info(1,2,3,4,5,6)

def s(**kwargs):
    print(kwargs)
s(a=1)
s(a=1,b=2,c=3)

def info(m,n,*args,f=666,**kwargs):
    print(m)
    print(n)
    print(args)
    print(kwargs)
    print(f)
info(1,2,3,4,5,f=888,a=1,b=2,c=3)