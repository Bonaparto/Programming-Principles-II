import re

# a, b = input(), input()
# l = a.find(b)
# if l == -1:
#     print('Not found')
# else:
#     print('First time', b, 'occured in position:', l)

a, b, pos = input(), input(), 'Not Found'
if b in a:
    pos = re.search(f"{b}", a).span()[0]
print(f"First time {b} occured in position: {pos}" if pos != 'Not Found' else 'Not found')