a = input().split()
c, b = int(a[0]), int(a[1])

if int(a[0]) < 1000:
    c = 1000
if int(a[1]) > 10000:
    b = 10000
if c <= 2187 and 6561 <= b:
    print(6561, 2187)
elif c <= 2187 <= b < 6561:
    print(2187)
elif c <= 6561 <= b:
    print(6561)