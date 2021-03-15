a, b = map(int, input().split())
cnt = 0
while True:
    if a > b:
        print(cnt)
        break
    cnt += 1
    a *= 3
    b *= 2