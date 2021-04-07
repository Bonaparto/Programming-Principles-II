# объявление функции
def is_correct_bracket(text):
    if text[0] == ')' or text[-1] == '(':
        return False
    temp_text = text.split('(')
    temp_text1 = text.split(')')
    print(temp_text)
    return len(temp_text) == len(temp_text1)

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))