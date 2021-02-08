n, a = int(input()), int(input())
ans = (n * a) ** 0.5
for i in range(n - 1, 0, -1):
    ans += (i * a)
    ans = ans ** 0.5
print(ans)