x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))


def average():
    if x > y:
        if z > x: return x
        elif y < z: return z
        else: return y
    elif z > y: return y
    elif z < x: return x
    return z


print(average())

