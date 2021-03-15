n = input()
l = input().split()
n = list(input())
n.clear()
l1 = input().split()
for i in l:
    if i not in l1:
        n.append(i)
n1 = []
for i in l1:
    if i not in l:
        n1.append(i)
print('Missed students:')
for i in n:
    print('-', i)
print('Not in the group:')
for i in n1:
    print('-', i)