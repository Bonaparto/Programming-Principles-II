a = input().split()
a, b = int(a[0]), int(a[1])

def IsPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
ans = []
for i in range(a, b+1):
    if IsPrime(i) and i != 1:
        ans.append(i)
ans.sort(reverse=1)
print(*ans)