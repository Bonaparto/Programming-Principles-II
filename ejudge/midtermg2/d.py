s = input()
x, y = map(int, input().split())
for i in s:
    if x == 0 and y == 0:
        print('Passed')
        break
    if i == 'R':
        x -= 1
    if i == 'L':
        x += 1
    if i == 'D':
        y += 1
    if i == 'U':
        y -= 1
    if x == 0 and y == 0:
        print('Passed')
        break
else:
    print('Missed')