# объявление функции
def draw_triangle():
    for i in range(8):
        for j in range(1, 16):
            if j <= 8 + i and j >= 8 - i:
                print('*', end='')
            elif j < 8 + i:
                print(' ', end='')
        print()

# основная программа
draw_triangle()  # вызов функции