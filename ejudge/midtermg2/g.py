import re
txt, t, s, f = input(), input(), input(), input()
txt = re.sub(f"{t}", f"{s}", txt)
print(len(re.findall(f"{f}", txt)))  