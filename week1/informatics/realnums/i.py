p, x, y, k = int(input()), int(input()), int(input()), int(input())
x += (y / 100)
for i in range(k):
    x += (x * p) / 100
    x *= 100
    x = int(x)
    x /= 100
print(int(x), int(x * 100) % 10 + (int(x * 10) % 10) * 10)