from sys import stdin

s = sorted(input())
ss = stdin.read().splitlines()

ans = []

for i in ss:
    w = ''
    for j in i:
        w += j
    if sorted(w) != s:
        ans.append(w)

ans.sort()
print(*ans)