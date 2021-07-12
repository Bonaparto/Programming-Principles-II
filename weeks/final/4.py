n = [i for i in input().split()]
s = []
for i in range(len(n)):
    if n[i] == n[i][::-1]:
        continue
    if n[i] not in s:
        s.append(n[i])
print(*sorted(s), sep='\n')