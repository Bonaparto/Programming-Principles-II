n, m = map(int, input().split())
N = set(int(input()) for i in range(n))
M = set(int(input()) for i in range(m))

I = N.intersection(M)
N, M = sorted(N), sorted(M)

print(len(I))
print(*sorted(I))

N1, M1 = [], []

for i in range(len(N)):
    if N[i] not in I:
        N1.append(N[i])
for i in range(len(M)):
    if M[i] not in I:
        M1.append(M[i])

print(len(N1))
print(*N1)
print(len(M1))
print(*M1)


# A & B - INTERSECTION
# A - B - nums in A, which are not in B