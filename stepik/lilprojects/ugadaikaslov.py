from random import *

word_list = ['даун', 'дурак', 'далбич', 'додик', 'жылан', 'овощ', 'канагаттандырылмагандытарыныздан', 'махаббат']

def get_word():
    return choice(word_list).upper()

def display_hangman(tries):
    stages = [  
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  
    guessed = False                    
    guessed_letters = []               
    guessed_words = []                 
    tries = 6  
    f = True
    print('Давайте играть в угадайку слов!')
    while f:
        print('Прогресс слова:')
        print(word_completion)
        print(f'Road to the hell is {6-tries}/6')
        print(display_hangman(tries))
        x = ''
        while True:
            print('Введите букву.')
            x = input()
            if not x.isalpha():
                print('Вы ввели недопустимый символ.')
                continue
            if x in guessed_letters:
                print('Вы уже угадали эту букву.')
                continue
            break
        tries -= 1 
        if x in word:
            print('Вы угадали букву.')
            guessed_letters.append(x)
            n = word.find(x)
            # for i in range(len(word_completion)):            Need to replace the '_' with a letter.
                    
            if word_completion == word:
                print('Вы победили!!11!1')
                print(f'Загаданное слово было: {word}')
                break
        else:
            if tries == 0:
                print('Лузер.')
                print(f'Загаданное слово было: {word}')
                print(display_hangman(tries))
                break
            print('Какая жалость.')
  
play(get_word())