# Способ 1
# Сохранять простые числа по пути, так как они являются делителями
# Проверять делимость на них только для значения <= корня из проверяемого
# Проверять только нечетные
from math import sqrt
from time import time


def find_prime(n):
    if n == 1: return 2
    prime = [2]
    current = 3
    middle = round(sqrt(current))

    while len(prime) < n:
        is_prime = True
        for i in prime:
            if i <= middle and current % i == 0:
                is_prime = False
                break

        if is_prime: prime.append(current)
        current += 2
        middle = round(sqrt(current))

    return prime[-1]


start_time = time()
print(find_prime(10000), f'For time = {time() - start_time}')
# n = 10000
# 104729 For time = 16.562620878219604 # Если квадратный корень выслять во вложенном цикле
# 104729 For time = 4.144850015640259 # Если проверку на него убрать
# 104729 For time = 2.0064499378204346 # Если соххранять в пременную


def eratosthenes(n):
    # Ищу до exp(sqrt(n)), посмотрела график зависимости простых числе от номера, он ниже этой функции
    # a = [i for i in range(2, max(50, int(exp(sqrt(n))) + 1), 1)]
    a = [i for i in range(2, n**2, 1)]
    prime_count = 0
    for elem in a:
        if elem == 0: continue

        prime_count += 1
        for i in range(elem * 2 - 2, len(a), elem):
            a[i] = 0
        if prime_count == n: return elem


start_time = time()
print(eratosthenes(10000), f'For time = {time() - start_time}')
# n = 10000
# 104729 For time = 49.26876497268677

