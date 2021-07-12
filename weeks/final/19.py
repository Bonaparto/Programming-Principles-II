n = int(input())
s = [int(i) for i in input().split()]
for i in s:
    if i == max(s):
        print(1, end=' ')
    else:
        print(0, end=' ')
