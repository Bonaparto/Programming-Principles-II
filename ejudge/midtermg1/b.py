import re

s = input()
p1 = r'[\W]'
print('Not matched!' if re.search(p1, s) else 'Found a match!')