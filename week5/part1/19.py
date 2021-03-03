import os

p = os.getcwd() + '/week5/part1/'
ans = []
for i in os.listdir(p):
    i_path = os.path.join(p, i)
    if os.path.isfile(i_path):
        with open(i_path, 'r', encoding='utf-8') as f:
            l = f.read()
            ans.append(l)
print(ans)