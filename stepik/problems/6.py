# объявление функции
def is_palindrome(text):
    temp_text = ''
    for i in text:
        if i.isalpha():
            temp_text += i.lower()
    return temp_text == temp_text[::-1]
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))