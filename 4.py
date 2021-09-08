from random import randint, uniform

alphabet = 'abcdefghijklmnopqrstuvwxyz'
a = input('Введите начало диапазона: ')
b = input('Введите конец диапазона: ')

try:
    print(f'Ваше случайное число {randint(int(a), int(b))}')
except: pass

try:
    print(f'Ваше случайное число {uniform(float(a), float(b))}')
except: pass

try:
    a = alphabet.index(a.lower())
    b = alphabet.index(b.lower())
    print(f'Ваша случайная буква {alphabet[randint(a, b)]}')
except:
    print('Нужно было ввести либо два числа, либо две буквы внглийского алфавита')
