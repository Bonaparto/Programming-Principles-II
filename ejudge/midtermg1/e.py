c = {}
for i in range(int(input())):
    s = input()
    s1 = s[:s.find(' ')]
    c[s1] = s[s.find(' ')+1:].split()
for i in range(int(input())):
    x, f = input(), True
    for j in c.keys():
        if x in c[j]:
            print(j)
            f = False
            break
    if f:
        print('Unknown')
