s = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
ans = {}
for i in sorted(s):
    if i in ans.keys():
        ans[i] += 1
    else:
        ans[i] = 1

print(len(ans))
for i in ans.keys():
    print(i, ans[i])