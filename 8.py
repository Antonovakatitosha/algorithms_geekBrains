from functools import reduce

a = []

for i in range(4):
    line = input("Введите 4 элемента через пробел: ").split(' ')
    line = list(map(lambda elem: int(elem), line))
    line.append(reduce(lambda x, y: x + y, line))
    a.append(line)

print(a)
