n, k = map(int, input().split())
for i in range(n):
    s = list(map(int, input().split()))
    avg = 0
    for i in s:
        avg += i
    if avg / 3 >= k:
        print('YES')
        break
else:
    print('NO')
