n = [int(i) for i in input().split()]
a, b = n[0], n[1]

for i in range(a):
    f = False
    if i < a // 2:
        f = True
    for j in range(b):
        if f and j < b // 2:
            print(1, end=' ')
        elif f and j >= b // 2:
            print(0, end=' ')
        elif not f and j < b // 2:
            print(2, end=' ')
        elif not f and j >= b // 2:
            print(3, end=' ')
    print()