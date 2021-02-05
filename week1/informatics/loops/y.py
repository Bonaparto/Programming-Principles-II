n = int(input())
l = n
for i in range(1, n + 1):
    if(i > l):
        print((str(i) + ' ') * l)
        break
    print((str(i) + ' ') * i, end='')
    l -= i