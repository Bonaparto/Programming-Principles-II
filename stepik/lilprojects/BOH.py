# BOH - Binary, Octal, Hex

n = int(input())
print(bin(n)[2:], oct(n)[2:], hex(n)[2:].upper(), sep='\n')
# while n:
#     n, r = divmod(n, 2)
#     sr = str(r) if r < 10 else str(chr(ord('A') + r - 10))
#     ans = sr + ans
# print(ans)