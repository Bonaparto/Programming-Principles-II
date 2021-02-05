n = int(input())
print(int((n % 10) == (n // 1000) and ((n // 10) % 10) == ((n // 100) % 10)))