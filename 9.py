from functools import reduce
a = []
n = int(input('Введите количество чисел: '))

for i in range(n): a.append(input(f"{i + 1} число: "))


def number_sum(string):
    return reduce(lambda prev, current: prev + int(current), string, 0)


max_sum, number = reduce(
    lambda prev, current: prev if number_sum(current) < prev[0] else (number_sum(current), current), a, (0, 0))

print(f'Число {number}, сумма цифр {max_sum}')
