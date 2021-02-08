s = input()
s1 = s[:s.find('h')+1]
s2 = s[len(s) - s[-1::-1].find('h') - 1:]
print(s1, s[(s.find('h') + 1):len(s) - s[-1::-1].find('h') - 1].replace('h', 'H'), s2, sep='')