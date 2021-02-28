import re
p1 = r'\w+ (<[a-zA-Z]{1}[\w._-]+?@[a-z]+.[a-z]{1,3}>)'
for i in range(int(input())):
    s = input()
    if re.search(p1, s):
        print(s)