n = int(input())
n1 = n
cur,a,b = map(int,input().split())
mod = 1791791791
def NextRand():
    global cur
    cur = (cur * a + b) % mod
    return cur
def List():
    list = []
    for i in range(n):
        list.append(NextRand())
    return list
def CompareList():
    return List()
def MaxValue():
    max_v = max(List())
    return max_v
def SecondMax():
    List().remove(MaxValue())
    second = max(List())
    return second
print(List())