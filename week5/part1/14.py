import os
from random import randint

p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    l = f.readlines()
with open(p+'text3.txt', 'r', encoding='utf=8') as f1:
    l1 = f1.readlines()
n = int(input())
for i in l:
    print(i + ' ' + l1[n])