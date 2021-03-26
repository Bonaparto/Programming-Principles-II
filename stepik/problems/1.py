# put your python code here
s = input()
count = 0
for i in range(len(s)):
    if s[i] == 'f':
        count += 1
    if count == 2:
        print(i)
        break
if count == 0:
    print(-2)
elif count == 1:
    print(-1)