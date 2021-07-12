n = [int(i) for i in input().split()]
a, b, c = n[0], n[1], n[2]

m = a - b
k = (m + (b - c) - 1) / (b - c)

print(int(k + 1))