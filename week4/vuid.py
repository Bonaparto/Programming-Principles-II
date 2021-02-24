import  re


pattern = re.compile(r'[A-Z]{2,}[0-9]{3,}[a-z]*')
for i in range(int(input())):
    s = input()
    print(pattern.findall(s))