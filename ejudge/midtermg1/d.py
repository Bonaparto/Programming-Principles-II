from sys import stdin

l, ans = stdin.readlines(), {}
for i in l:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1
a = []
for i in ans.keys():
    if ans[i] % 2 == 0:
        a.append(i)
print(*sorted(a), sep='', end='')