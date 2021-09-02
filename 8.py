from functools import reduce

x = input('Введите цифру, которую будем искать: ')
n = int(input('Введите количество чисел: '))

a = []
for i in range(n): a.append(input(f"{i + 1} число: "))
print(reduce(lambda prev, current: prev + current.count(x), a, 0))


