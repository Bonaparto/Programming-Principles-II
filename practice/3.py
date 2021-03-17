adress = input().split('.')
for i in adress:
    try:
        i = int(i)
        if 0 <= i <= 255:
            continue
        else:
            print('0')
            raise SystemExit
print('1')