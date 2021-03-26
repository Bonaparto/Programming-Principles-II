def Eencrypt(text, shift):
    ans = ''
    for i in text:
        if ord('A') > ord(i) or ord('Z') < ord(i): 
            ans += i
        elif ord(i) + shift <= ord('Z'):
            ans += chr(ord(i) + shift)
        else:
            ans += chr(ord('A') - 1 + shift + ord(i) - ord('Z'))
    return ans

def Edecrypt(text, shift):
    ans = ''
    for i in text:
        if ord('A') > ord(i) or ord('Z') < ord(i): 
            ans += i
        elif ord(i) - shift >= ord('A'):
            ans += chr(ord(i) - shift)
        else:
            ans += chr(ord('Z') + 1 - ord('A') + ord(i) - shift)
    return ans

def Rencrypt(text, shift):
    r, ans = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', ''
    for i in text:
        if r.find(i) != -1:
            ans += r[(r.find(i) + shift) % len(r)]
        else:
            ans += i
    return ans

def Rdecrypt(text, shift):
    r, ans = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', ''
    for i in text:
        if r.find(i) != -1:
            if r.find(i) - shift < 0:
                ans += r[len(r) - abs(r.find(i) - shift)]
            else:
                ans += r[r.find(i) - shift]
        else:
            ans += i
    return ans

print('Print "1" if you want to encrypt the text.')
print('Print "2" if you want to decrypt the text.')
eord = int(input())

print('Print "R" for russian language.')
print('Print "E" for english language.')
language = input()

print('OK! Now print the number to shift.')
shift = int(input())

print('Print the text.')
text = input()

if language == 'E':
    if eord == 1:
        enc_text = Eencrypt(text.upper(), shift)
        print('Here is your enrypted text:')
        for i in range(len(enc_text)):
            if text[i].isupper():
                print(enc_text[i], end='')
            else:
                print(enc_text[i].lower(), end='')
    else:
        dec_text = Edecrypt(text.upper(), shift)
        print('Here is your decrypted text:')
        for i in range(len(dec_text)):
            if text[i].isupper():
                print(dec_text[i], end='')
            else:
                print(dec_text[i].lower(), end='')
else:
    if eord == 1:
        enc_text = Rencrypt(text.upper(), shift)
        print('Here is your enrypted text:')
        for i in range(len(enc_text)):
            if text[i].isupper():
                print(enc_text[i], end='')
            else:
                print(enc_text[i].lower(), end='')
    else:
        dec_text = Rdecrypt(text.upper(), shift)
        print('Here is your decrypted text:')
        for i in range(len(dec_text)):
            if text[i].isupper():
                print(dec_text[i], end='')
            else:
                print(dec_text[i].lower(), end='')