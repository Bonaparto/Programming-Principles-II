from sys import stdin

a = stdin.read().split()
alp = 'abcdefghijklmnopqrstuvwxyz'
l = {}
for i in alp:
    l[i] = 0
for i in a:
    i = i.lower()
    i = i[0]
    if i not in alp and not i in alp.upper():
        continue
    if i in l.keys():
        l[i] += 1
    else:
        l[i] = 1

for i in l.keys():
    print(l[i])