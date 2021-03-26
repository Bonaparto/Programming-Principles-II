import random

def generate_password(c, l):
    print(*random.sample(c, l), sep='')

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('How many passwords do you need?')
amount = int(input())

print('Enter the length of passwords.')
plength = int(input())

print('Choose what the password(s) should contain.')
print('Enter "1" to add and "2" otherwise.\n')

print('Should password contain digits?')
if input() == '1':
    chars += digits

print('Should password contain uppercase letters?')
if input() == '1':
    chars += uppercase_letters

print('Should password contain lowercase letters?')
if input() == '1':
    chars += lowercase_letters

print('Should password contain symbols?')
if input() == '1':
    chars += punctuation

print('Should password contain confusable characters (il1Lo0O)?')
if input() == '1':
    chars += 'il1Lo0O'

print('Generating in process...')

for i in range(amount):
    generate_password(chars, plength)

print('Everything is done!')