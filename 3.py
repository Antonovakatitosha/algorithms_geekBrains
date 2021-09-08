a = input('Введите число: ')
result = ''

while len(a) > 0:
    result += a[-1]
    a = a[:-1]

print(result)