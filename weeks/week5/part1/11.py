import os
p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    l = f.read()
    l1 = l.split('\n')
print(len(l) + len(l1) - 1)