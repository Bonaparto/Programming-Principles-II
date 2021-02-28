import re

with open('Py3\Programming-Principles-II\week4\\text.txt', 'r', encoding = 'utf-8') as f:
    txt = f.read()

pattern = re.compile(r'ТОО ([\w]+)')      # Name of the company

name = pattern.findall(txt)[0]
print('Name of the company:', name)


pattern = re.compile(r'БИН ([\d]+)')       # БИН

BIN = pattern.findall(txt)[0]
print('BIN of the company:', BIN)

pattern = re.compile(r'( ?[a-zA-ZА-Яа-я0-9%.\,\(\)\[\]]+( ?[\w%.\,\(\)\[\]]+)+)')          #   Name of the products (Not finished)
products = pattern.findall(txt)
print(products)

pattern = re.compile(r'(Время:) (\d{2}.\d{2}.\d{4}) (\d{2}:\d{2}:\d{2})')      # Date and time

date = pattern.findall(txt)[0][1]
time = pattern.findall(txt)[0][2]
print('Date:', date)
print('Time:', time)


pattern = re.compile(r'(г. ([a-zA-ZА-Яа-я0-9\-\, ]+)+)')          # Adress, but only name of the city

adress = pattern.findall(txt)[0]
print('Adress:', adress[0])