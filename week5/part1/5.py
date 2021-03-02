import os
p = os.getcwd() + '/week5/part1/'
l = []
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
print(l)