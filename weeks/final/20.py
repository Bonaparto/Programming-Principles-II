n = [int(i) for i in input().split()]
x = -max(n)
while True:
    if n[0] * x - n[1] == n[2] * x + n[3]:
        print(x)
        break
    x += 1