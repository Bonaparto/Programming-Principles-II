l = [int(i) for i in input().split()]
a, b = int(l[0]), int(l[1])
n, ans, max_v = 0, 0, 0
for i in range(a):
    n = 0
    for k in [int(i) for i in input().split()]:
        n += k
    if n > ans:
        ans = n
        max_v = i + 1
print(max_v)