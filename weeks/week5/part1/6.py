import os
p = os.getcwd() + '/week5/part1/'
l, l1 = [], ''
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
for i in l:
    l1 += i
print(l1)