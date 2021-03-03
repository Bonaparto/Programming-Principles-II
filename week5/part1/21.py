import os

p = os.getcwd() + '/week5/part1/'
n, k = int(input()), 0
with open(p + 'text4.txt', 'w', encoding='utf-8') as f:
    while True:
        s = ''
        for i in range(1, n+1):
            s += chr(65+k)
            k += 1
            if(k == 26):
                break
        if(k == 26):
            f.write(s)
            break
        s += '\n'
        f.write(s)