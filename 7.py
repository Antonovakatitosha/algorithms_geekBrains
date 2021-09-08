n = int(input('Введите количество членов прогрессии: '))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f"1 + 2 + ... + n = {sum}\nn * (n + 1) / 2 = {int(n * (n + 1)/2)}")
