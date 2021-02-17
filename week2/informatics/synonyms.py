s = {}
for i in range(int(input())):
    a = input().split()
    s.update({a[0]:a[1]})

l = input()

if l in s.keys():
    print(s[l])
else:
    for i in s.keys():
        if s[i] == l:
            print(i)