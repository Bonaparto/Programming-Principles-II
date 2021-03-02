import os
from collections import Counter
p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    l = f.read()
l.replace('.', ' ')
l.replace(',', ' ')
l.replace('?', ' ')
l.replace('!', ' ')
l = l.split()
print(Counter(l))