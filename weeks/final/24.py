total, scores = 0, {}
for i in range(int(input())):
    s = input().split()
    a, b = s[0], int(s[1])
    if a not in scores.keys():
        scores[a] = b
    else:
        scores[a] += b
    total += b
ss = []
for i in scores.keys():
    ss.append(scores[i])

ss = sorted(ss, reverse=1)
for i in ss:
    for j in scores.keys():
        if i == scores[j]:
            ans = round((scores[j] * 100) / total, 5)
            if len(str(ans)) > 7:
                print(j, round(ans, len(str(ans)) - 2 - len(str(int(ans)))), end='')
            elif str(ans)[len(str(ans)) - 1] == '0':
                print(j, int(ans), end='')
            else:
                print(j, ans, end='')
    print('%')