def degree(x, y):
    if y == 1:
        return x
    if y == 0:
        return 1
    if y % 2 == 0:
        return degree(x * x, y / 2)
    else:
        return degree(x, 1) * degree(x, y - 1)
print(degree(float(input()), int(input())))