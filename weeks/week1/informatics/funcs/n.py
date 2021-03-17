def sol(a, b):
    if(b == 1):
        return a
    if(a == b or b == 0):
        return 1
    return (sol(a - 1, b - 1) + sol(a - 1, b))

print(int(sol(int(input()), int(input()))))