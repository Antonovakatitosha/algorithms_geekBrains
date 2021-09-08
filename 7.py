def triangle():

    x = int(input('Введите длину первого отрезка: '))
    y = int(input('Введите длину второго отрезка: '))
    z = int(input('Введите длину третьего отрезка: '))

    if x + y <= z or y + z <= x or x + z <= y:
        return "Треугольник не существует"

    if x == y or y == z or z == x:
        if x == y == z: return "Равносторонний"
        return "Равнобедренный"

    return "Разносторонний"


print(triangle())
