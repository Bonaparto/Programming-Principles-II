a = input().split() 
print(*(int(i) for i in a if i != '0'), '0 ' * a.count('0'))