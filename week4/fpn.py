import  re

p1 = r'^(\+|-)\d+\.\d+'
p2 = r'(\+|-)\.\d+'
p4 = r'(^\d+\.\d+$)'
p3 = r'[^+-.\d]'

for i in range(int(input())):
    s = input()
    if re.search(p3, s):
        print(False)
        continue    
    if re.search(p2, s) or re.search(p1, s) or re.search(p4, s):
        print(True)
    else:
        print(False)