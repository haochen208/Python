def eatcarrot(n,m):
    old = [i for i in range(1,n+1)]
    new=[]
    index= m-1
    while len(old) > 0:
        if len(old) <= m:
            index = (m-1) % len(old)
        new.append(old.pop(index))
        old= old[index:] + old[:index]
    return new
print(eatcarrot(15,3))