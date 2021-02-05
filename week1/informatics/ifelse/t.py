n = int(input())
cnt1, cnt2, cnt3, n1 = 0, 0, 0, n
if(n1 >= 35):
    if(n1 % 60 >= 35):
        print(0, 0, (n1 // 60) + 1)
        raise SystemExit
    else:
        n1 -= (n1 // 60) * 60
        cnt3 += (n // 60)
n = n1
if(n1 >= 9):
    if(n1 % 10 == 9):
        print(0, (n1 // 10) + 1, cnt3)
        raise SystemExit
    n1 -= ((n1 // 10) * 10)
    cnt2 += (n // 10)
cnt1 += n1 
print(cnt1, cnt2, cnt3)