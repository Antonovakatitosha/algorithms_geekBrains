def equations():
    x1 = int(input('Введите координаты первой точки\n'))
    y1 = int(input())
    print(f'Первая точка ({x1}, {y1})')

    x2 = int(input('Введите координаты второй точки\n'))
    y2 = int(input())
    print(f'Вторая точка ({x2}, {y2})')

    res_str = 'Через данные точки проходит прямая:'

    if y1 == y2 and x1 == x2:
        return f'Через данные точки проходит бесконечное множество прямых'
    if y1 == y2: return f'{res_str} y = {y1}'
    if x1 == x2: return f'{res_str} x = {x1}'

    k = round((y1 - y2) / (x1 - x2), 1)
    b = y1 - k * x1

    print(k, b)

    if b == 0: return f'{res_str} y = {"" if k == 1 else k}x'
    else:
        return f'{res_str} y = {"" if k == 1 else k}x {"+" if b > 0 else "-"} {abs(b)}'


print(equations())
