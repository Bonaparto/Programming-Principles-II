from math import log2
a = [int(i) for i in input().split()]
s = []
for i in a:
    if i % 2 != 0 and i != 1 and i not in s:
        s.append(i)
        continue
    n, f = 1, False
    while True:
        if n == i:
            f = True
            break
        if n > i:
            break
        n *= 2
    if not f and i not in s:
        s.append(i)

print(*sorted(s))