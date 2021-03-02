import os
n = int(input())
p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    l = f.read().split('\n')
    ans = l[len(l)-n:]
print(*ans, sep='\n')