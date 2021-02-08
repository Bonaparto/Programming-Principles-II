x, x1, cnt, ans = int(input()), 0, 1, 0
while(x != 0):
    x1 = int(input())
    if(x1 != x and x1 != 0):
        cnt += 1
    else:
        if(cnt > ans):
            ans = cnt
        cnt = 0
    x = x1
print(ans)