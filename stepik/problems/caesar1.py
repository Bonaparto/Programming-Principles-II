def encrypt(text, shift):
    ans = ''
    for i in text:
        # print(i)
        if ord('A') > ord(i) or ord('Z') < ord(i): 
            ans += i
        elif ord(i) + shift <= ord('Z'):
            ans += chr(ord(i) + shift)
        else:
            ans += chr(ord('A') - 1 + shift + ord(i) - ord('Z'))
    return ans

text, cnt, cnt1 = input().split(), 0, 0
for j in text:
    for k in j:
        if k.isalpha():
            cnt1 += 1
    enc = encrypt(j.upper(), cnt1)
    for i in enc:
        if j[cnt].isupper():
            print(i, end='')
        else:
            print(i.lower(), end='')
        cnt += 1
    print(end=' ')
    cnt = 0
    cnt1 = 0