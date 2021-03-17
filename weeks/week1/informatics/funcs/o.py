def ans(x):
    if x == 0:
        return x
    a = int(input())
    if a == 0:
        return x
    return ans(x + a)
print(ans(int(input())))