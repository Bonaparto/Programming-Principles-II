import re

repeat = r'(.)*(\1)'
ints = r'[\d]{3,}'
chars = r'[A-Z]{2,}'

for i in range(int(input())):
    n = sorted(input())  
    n = ''.join(n)
    if len(n) == 10:
        if re.search(chars, n) and re.search(ints, n) and not re.search(repeat, n):
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')