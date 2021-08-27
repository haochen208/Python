# 从字符串'abcdefghijklmnopqrstuvwxyz'中随机抽取两个字母组成字符串,共挑选一百个,降序输出所有不同的字符串及其重复次数.

import random

s = 'abcdefghijklmnopqrstuvwxyz'
d = {}
for i in range(100):
    ins = ''.join(random.sample(s, 2))
    d[ins] = d.get(ins, 0) + 1

for j in reversed(sorted(d.keys())):
    print(j, end=' ')
    print('Repeat {} times'.format(d[j]))