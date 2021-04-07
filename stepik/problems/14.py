lines = []
for i in range(int(input())):
    lines.append(input())
x = int(input())
for i in range(len(lines)):
    print(len(lines[i]))
    if x - 1 < len(lines[i]):
        print(lines[i][x-1], end='')