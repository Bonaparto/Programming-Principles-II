n, l, s, s1 = int(input()), input().split(), '', ''
k = int(input())
if(k == 0):
    print(0)
else:
    for i in range(len(l)):
        if i > k - 1:
            s1 += l[i]
        else:
            s += l[i]
    print(int(s) * int(s1))