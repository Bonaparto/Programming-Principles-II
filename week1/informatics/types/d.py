pi = 0
for i in range(0, 10):
    if i % 2 == 0:
        pi += (4 / (1 + i * 2))
    else:
        pi -= (4 / (1 + i * 2))
print(pi)