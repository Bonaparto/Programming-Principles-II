import re

n = input()
l = re.split(r',|\.', n)
for i in l:
    print(i)