n, s = int(input()), input()
for i in s:
    if ord(i) - n < 97:
        print(chr(26 + ord(i) - n), end='')
    else:
        print(chr(ord(i) - n), end='')