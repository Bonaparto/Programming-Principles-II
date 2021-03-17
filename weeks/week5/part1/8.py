import os
p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    l = f.read().split()
mx = len(max(l, key=len))
print(*[i for i in l if len(i) == mx])