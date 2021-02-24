from enum import EnumMeta
import re

pattern = re.compile(r'[+-.]?[\d]+.[\d]{1,}')
for i in range(int(input())):
    s = input()
    if pattern.search(s):
        print('True')
    else: 
        print('False')