# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    else:
        dig, up, dn = False, False, False
        for i in password:
            if i.isupper():
                up = True
            if i.isdigit():
                dig = True
            if i.islower():
                dn = True
        return dig and up and dn       
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))