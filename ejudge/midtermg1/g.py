a = []
for i in range(int(input())):
    a.append(sorted(set(input())))
ans = []
for i in a[0]:
    for j in range(1, len(a)):
        if i not in a[j]:
            break
    else:
        ans.append(i)
if len(ans) == 0:
    print('NO COMMON CHARACTERS')
else:
    print(*ans)