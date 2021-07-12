from sys import stdin

a = stdin.read().split()
ans = {}

for i in range(0, len(a)-1, 2):
    if a[i] not in ans.keys() or ans[a[i]] < int(a[i+1]):
        ans[a[i]] = int(a[i+1]) 
ans1 = sorted(ans.keys())

for i in ans1:
    for j in ans.keys():
        if ans[j] == ans[i]:
            print(i, ans[j])
            break