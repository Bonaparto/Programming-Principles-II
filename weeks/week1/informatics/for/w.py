a, b, c, d = int(input()), int(input()), int(input()), int(input())
i, f = a, True
l = (a // d)
while(i in range(a, b + 1) and f):
    s = (l + i - a) * d
    g = s + c
    while(s % d == 0 and g <= b and s >= a):
        print(g, end=' ')
        g += d
    while(g > b):
        g = 0
        f = False
    i += 1