def rev(x):
    if x == 0:
        print(0)
        return x
    rev(int(input()))
    print(x)
rev(int(input()))