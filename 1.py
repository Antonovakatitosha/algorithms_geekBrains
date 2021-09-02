def calculator():
    while True:

        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))

        while True:
            sign = input('Введите знак операции или 0 для выхода: ')

            if sign == '0': return
            if sign not in ['+', '-', '*', '/']: print('Ошибка')
            else: break

        if sign == '/':
            if b == 0: print('Деление на ноль здесь невозможно')
            else: print(a / b)

        if sign == '*': print(a * b)
        if sign == '-': print(a - b)
        if sign == '+': print(a + b)


calculator()
