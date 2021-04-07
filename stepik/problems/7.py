# объявление функции
def is_valid_password(password):
    n = [int(i) for i in password.split(':')]
    s = str(n[0])
    if s != s[::-1]:
        return False
    for i in range(2, round(n[1] ** 0.5) + 1):
        if n[1] % i == 0:
            return False
    return n[2] % 2 == 0

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))