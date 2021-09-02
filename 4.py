a = int(input('Введите количество членов прогрессии: '))

current = 1
step = -2
sum = 0

for i in range(a):
    sum += current
    current /= step

print(sum)

