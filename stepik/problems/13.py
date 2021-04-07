# объявление функции
def is_pangram(text):
    s = ''
    ss = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    for i in text:
        if i in ss and i not in s:
            s += i
    return len(s) == 26

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))