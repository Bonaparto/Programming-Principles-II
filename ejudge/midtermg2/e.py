l = input().split()
k = max(len(i) for i in l)
for i in l:
    if len(i) == k:
        print(i)
        break
print(k)