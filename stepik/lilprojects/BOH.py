# BOH - Binary, Octal, Hex

n = int(input())

while n:
    n, r = divmod(n, 2)
    sr = str(r) if r < 10 else str(chr(ord('A') + r - 10))
    ans = sr + ans
print(ans)