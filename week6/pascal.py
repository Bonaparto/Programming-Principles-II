def pascal(n):
    a = [1 for i in range(n)]
    b = a.copy()
    for i in range(0, n):
        print(' ' * (n - i - 1), end='')
        for j in range(0, i+1):
            if(j != 0 and j != i):
                b[j] = a[j-1] + a[j]
            print(b[j], end=' ')
        a = b.copy()
        print()

pascal(int(input()))