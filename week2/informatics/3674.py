from sys import stdin

def comp(a):
    return(-a[0], a[1])

a = stdin.read().split()    #splitlines() creates a list of lines, not single words
l, b, c = {}, [], []

for i in a:
    if i not in b:
        c.append(f)
        f = (a.count(i), i)
        b.append(i)

for i in sorted(c, key=comp):
    print(i[1])

