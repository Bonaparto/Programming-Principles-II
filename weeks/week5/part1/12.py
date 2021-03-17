import os

l = input().split()
p = os.getcwd() + '/week5/part1/'
with open(p+'text2.txt', 'a', encoding='utf-8') as f:
    for i in l:
        f.write(i + ' ')