def to_seven(n):
    if n == 0:
        return 0 
    s = ''
    while n:
        a = n % 7
        s = str(a) + s
        n //= 7
    return s
print(to_seven(int(input())))