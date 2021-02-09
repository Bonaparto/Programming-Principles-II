a = input().split()
k = int(input())
if(k >= 0):
    if(k == 0 or k % len(a) == 0):
        print(*a)
    else:
        print(*(a[len(a)-k%len(a):]), *a[-len(a):-k%len(a)])
else:
    if(k % -len(a) == 0):
        print(*a)
    else: 
        print(*(a[-len(a)-k%-len(a):]), *a[:-k%-len(a)])