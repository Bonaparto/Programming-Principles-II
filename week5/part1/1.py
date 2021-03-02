import os
p = os.getcwd() + '/week5/part1/'
with open(p+'text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
print(text)