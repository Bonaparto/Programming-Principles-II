from sys import stdin

a = stdin.read().split()
s = {}

for i in a:
    if i not in s.keys():
        s[i] = 1
    else:
        s[i] += 1
# n = []
# for i in s.keys():
#     if s[i] not in n:
#         n.append(s[i])
# n = sorted(n)
l = sorted(s)
for i in l:
    print(i, s[i])