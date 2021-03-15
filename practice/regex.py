import re

txt = "the rain in         spain"
x = re.split("\s+", txt)
x = re.sub("\s+", " ", txt)
print(x)