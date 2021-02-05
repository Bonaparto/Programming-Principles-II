ans, n, prev = 0, int(input()), 1
for i in range(1, n + 1):
    prev *= i
    ans += prev 
print(ans)