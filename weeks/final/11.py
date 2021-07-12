from math import log2

a = [int(i) for i in input().split()]
ans = []
for i in a:
    if log2(i).is_integer() and i not in ans:
        ans.append(i)

print(*sorted(ans))