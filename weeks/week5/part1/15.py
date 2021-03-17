import os
from random import randint

p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
print(l[randint(0,len(l))], end='')