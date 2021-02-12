a = input().split() 
print(*(i for i in a if i != '0'), '0 ' * a.count('0'))