import os
n = int(input())
p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    for i in range(n):
        print(f.readline(), end='')