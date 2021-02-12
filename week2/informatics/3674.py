from sys import stdin
from operator import itemgetter

def comp(a, b):
    return(-a, b)

a = stdin.read().split()
l, b, c = {}, [], []
for i in a:
    l.update({i:a.count(i)})
    b.append(i)
b = set(b)
for i in b:
    c.append((int(l[i]), str(i)))
c.sort(comp)