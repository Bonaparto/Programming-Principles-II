n = [int(i) for i in input().split()]
a, b, c = n[0], n[1], n[2]
divs = []
for i in range(1, n[1]+1):
    if a % i == 0 == b % i:
        divs.append(i)
print(divs[len(divs) - c])