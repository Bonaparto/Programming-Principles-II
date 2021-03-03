import os

p = os.getcwd() + '/week5/part1/'
l = open(p+'text.txt', 'r', encoding='utf-8')
l.close()
print('The file is closed' if l.closed else 'The file is not closed')