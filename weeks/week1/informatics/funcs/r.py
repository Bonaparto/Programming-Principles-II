def gcd(a, b):
    if(a % b == 0):
        print(b)
        quit()
    return gcd(b, a % b)
gcd(int(input()), int(input()))