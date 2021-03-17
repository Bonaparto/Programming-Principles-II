import random

def is_valid(x):
    if not x.isdigit():
        return False
    return 1 <= int(x) <= 100

def is_valid1(x):
    return x == '1' or x == '2'

def game(n1, n):
    if n1 < n:
        print('Ваше число меньше загаданного, попробуйте еще разок.')
    elif n1 > n:
        print('Ваше число больше загаданного, попробуйте еще разок.')
    else:
        return True
    return False

n = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку.')
f, cnt = True, 0

while f:
    print('Введите любое число от 1 до 100.')
    n1 = input()

    if not is_valid(n1):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

    cnt += 1

    if game(int(n1), n):
        print(f'Вы угадали с {cnt} попытки, поздравляем!')
        f1 = True
        while f1:
            print('Введите "1", чтобы продолжить игру.')
            print('Введите "2", чтобы закончить игру.')
            ans = input()
            if not is_valid1(ans):
                print('Такой вариант не предусмотрен.')
            else:
                if ans == 1:
                    f1 = False
                else:
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    f1 = False
                    f = False