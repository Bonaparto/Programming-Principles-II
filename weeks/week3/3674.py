from sys import stdin

def comp(a):
    return(-a[0], a[1])

a = stdin.read().split()    #splitlines() creates a list of lines, not single words
l, b, c = {}, [], []

for i in a:
    if i not in b:
        f = (a.count(i), i)
        c.append(f)
        b.append(i)

for i in sorted(c, key=comp):
    print(i[1])