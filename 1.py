def sum_numbers():
    x = int(input('Введите трехзначное число\n'))

    if not 99 < x < 1000:
        return "Число не трехзначное"

    a = x % 10
    x = x // 10
    b = x % 10
    c = x // 10
    return a * b * c, a + b + c


print(sum_numbers())

