n = [int(i) for i in input().split()]
for i in n:
    if i != 0:
        print(i, end=' ') 
print('0 ' * n.count(0))