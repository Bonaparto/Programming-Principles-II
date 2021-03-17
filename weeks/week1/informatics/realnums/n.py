ans = 0
for i in range(1, int(input()) + 1):
    ans += (1 / i) * (-1) ** (i+1)
print(ans)