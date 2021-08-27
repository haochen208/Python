# 求1-2+3-4+5-6+7-8+......+97-98+99所有数的和。

sum = 0
for i in range(1,100):
    if i % 2 == 1:
        sum += i
    else:
        sum -= i

print(sum)

