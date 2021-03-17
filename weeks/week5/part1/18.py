import os

p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    t = [i.strip(',') for i in f.read()]
print(len(t))