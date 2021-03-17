import sys
sys.setrecursionlimit(10**7)

def count(s):
    l[s] += 1
    if(s in r):
        return
    count(tree[s])

tree, l, r = {}, {}, []
n = int(input())

for i in range(n - 1):
    a = input().split()
    if a[1] not in tree.values() and a[1] not in tree.keys():
        r.append(a[1])
        l.update({a[1]:0})
    tree.update({a[0]:a[1]})
    l.update({a[0]:0})
    count(a[1])

x = sorted(l.keys())

for i in x:
    print(i, l[i])
    