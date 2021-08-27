def blbble_soft(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] < l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
l=[98,65,88,42,66,12,32,89,56,55]
blbble_soft(l)
print(l)
