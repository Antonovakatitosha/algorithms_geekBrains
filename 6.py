from random import randint

a = randint(0, 100)
print(a)

for i in range(10):
    attempt = int(input("Введите ваше число: "))
    if attempt > a: print("Загаданое число меньше")
    elif attempt < a: print("Загаданое число больше")
    else:
        print("Угадали!")
        break
    print(f"Осталось попыток {10 - i - 1}")