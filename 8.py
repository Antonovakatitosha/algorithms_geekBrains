def year():
    date = int(input('Введите год: '))

    if date % 4 == 0 and (date % 100 != 0 or date % 400 == 0):
        return 'Високосный'
    return "Невисокосный"


print(year())
