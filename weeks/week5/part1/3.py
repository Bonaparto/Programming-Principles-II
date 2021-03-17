import os
p = os.getcwd() + '/week5/part1/'
f = open(p+'text.txt', 'a', encoding='utf-8')
f.write('\n'+input())
f = open(p+'text.txt', 'r', encoding='utf-8')
print(f.read())
f.close()