import os

p = os.getcwd() + '/week5/part1/task20/'
# os.chdir(p)
# os.mkdir(p, 'task20')
for i in range(26):
    with open(p + chr(65 + i) + '.py', 'w') as f:
        f.write('')