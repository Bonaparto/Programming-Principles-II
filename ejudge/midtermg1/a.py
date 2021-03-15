import re

s = input()
p1 = r'[A-Z][a-z]'
print('Found a match!' if re.search(p1, s) else 'Not matched!') 