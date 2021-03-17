cnt, n = 0, int(input())
for i in range(1, n):    
    cnt += i
    cnt -= int(input())
print(cnt + n)