alphabet = 'abcdefghijklmnopqrstuvwxyz'
a = input('Введите первую букву: ')
b = input('Введите вторую букыву: ')

a = alphabet.index(a.lower())
b = alphabet.index(b.lower())

print(f'Позийия первой буквы: {a + 1}\n'
      f'Позийия второй буквы: {b + 1}\n'
      f'Количество букв между ними: {b - a}')
