a = int(input('Введите натуральное число: '))
even_count = 0
odd_count = 0

while a > 0:
    if a % 10 % 2 == 0: even_count += 1
    else: odd_count += 1

    a //= 10

print(f'Четных {even_count}, нечетных {odd_count}')