import re

s = input()
p1 = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aoeiuAOEIU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
if re.search(p1, s):     
    for i in re.findall(p1, s):
        print(i)
else:
    print(-1)

