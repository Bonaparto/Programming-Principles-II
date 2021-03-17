import re
import csv

with open('Py3\Programming-Principles-II\week4\\text\\text.txt', 'r', encoding = 'utf-8') as f:
    txt = f.read()


compnamepat = re.findall(r'(?<=ТОО )[\w]+', txt)
compBINpat = re.findall(r'(?<=БИН )[\d]{12}', txt)

cntpat = re.findall(r'\d+\.\n', txt)
productsnamespat = re.findall(r'(.*)\n\d+,\d+ x \d+ ?\d+,\d+', txt)
amountofproduct = re.findall(r'(\d+),\d+ x \d+ ?\d+,\d+', txt)
priceofproduct = re.findall(r'\d+,\d+ x (\d+ ?\d+,\d+)', txt)
totalpriceofproducts = re.findall(r'Стоимость\n(\d+ ?\d+,\d+)', txt)

datepat = re.findall(r'Время: (\d{2}.\d{2}.\d{4} \d{2}:\d{2}:\d{2})', txt)
adresspat = re.findall(r'г\. (.*)', txt)

print('Name of the company:', *compnamepat)
print('BIN of the company:', *compBINpat)
print('List of bought items:')

items = [['Компания', 'БИН', "Название", "Количество", "Цена за единицу", "Сумма", "Дата", "Адрес"]]

for i in range(len(cntpat)):
    items.append((compnamepat[0], compBINpat[0], productsnamespat[i], amountofproduct[i], priceofproduct[i], totalpriceofproducts[i], datepat[0], adresspat[0]))
    print('Title:', productsnamespat[i])
    print('Count:', amountofproduct[i])
    print('Unit price:', priceofproduct[i])
    print('Total price', totalpriceofproducts[i])

print('Time:', *datepat)
print('Adress:', *adresspat)


with open('file.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(items)