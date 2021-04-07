# объявление функции
def convert_to_python_case(text):
    temp_text = ''
    for i in range(1, len(text)):
        if text[i].isupper():
            temp_text += '_'
        temp_text += text[i].lower()
    return temp_text

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))