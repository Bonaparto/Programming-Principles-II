for i in range(100, 1000):
    j = i ** 2
    l = str((j // 100) % 10) + str((j // 10) % 10) + str(j % 10)
    if(int(l) == i):
        print(i)