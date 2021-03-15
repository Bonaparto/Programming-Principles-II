import json
from sys import stdin

l = stdin.readlines()
s, ans = """""", {}
for i in l:
    s += i
s = json.loads(s)
min = int(s['Subscriptions'][0]['price'])
name = ''
for i in range(len(s['Subscriptions'])):
    f = int(s['Subscriptions'][i]['price'])
    d = int(s['Subscriptions'][i]['discount'])
    if f - (f * d) / 100 < min:
        min = f - (f * d) // 100
        name = s['Subscriptions'][i]['name']
print('Name:', name)
print('Price:', min)