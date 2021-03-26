import random

def choice():
    return random.randint(0, 19)

answers = ['жб', 'думаю да', 'хз', 'жынды ма?', 'стопудова', 'походу да', 'мб', 'кумаш', 'нанурсын так и есть', 'наверное', 'промолчу', 'нет бля', 'да', 'звезды говорят да', 'без понятия', 'нет', 'лариса экстрасенс сказала да', 'соси', 'спроси у', 'ты чорт']

print('Hello world, я шарик под именем жакс фреско, крутани меня и узнай ответ на любой вопрос.', 'Kak tebya zovut?', sep='\n')
name = input()
print(f'Shalom, {name}')
f = True

while f:
    print('Задай вопрос.')
    q = input()
    print(answers[choice()])
    print('Напиши "1", если у тебя еще есть вопросы.')
    print('Напиши "2", если ты пустоголовый.')
    ans = input()
    if ans == '1':
        continue
    elif ans == '2':
        f = False
        print('Ну и вали.')
    else:
        print('Один или два?')