from sys import stdin
def IsPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

n = stdin.read().split()
cnt = {}
for l in n:
    i = int(l)
    f = IsPrime(i)
    if f and i not in cnt.keys():
        cnt[i] = 1
    elif f:
        cnt[i] += 1
for i in cnt.keys():
    if cnt[i] > 1:
        print(i, end=' ')
    