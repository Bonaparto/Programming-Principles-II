a, i = int(input()), sorted(set(map(int, input().split())))
for j in range(len(i)):
    print(j+1, i[j])