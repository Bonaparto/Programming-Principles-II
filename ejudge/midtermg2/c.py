a = int(input())
b = list(map(int, input().split()))
print('YES' if a == len(set(b)) else 'NO')