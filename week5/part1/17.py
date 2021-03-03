import os

p = os.getcwd() + '/week5/part1/'
f = open(p+'text.txt', 'r', encoding='utf-8')
l = f.readlines()
l = [i.strip('\n') for i in l]
print(l)
f.closed()