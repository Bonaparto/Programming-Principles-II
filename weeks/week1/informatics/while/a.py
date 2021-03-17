n = int(input())
if(n > 0):
    print(((n + 1) * n) // 2)
if(n < 0):
    print(((((n - 1) * n) // 2) - 1) * -1)