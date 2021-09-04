# Версия python 3.8, разрядность системы 64x
#
# ЗАДАЧА 1
#
# start – 24 bytes
# end – 24 bytes
# i – 24 bytes
# j – 24 bytes
#
# суммарно 56 bytes, если под цикл не выделяется память, range итератор, как я поняла

start = 32
end = 127

for i in range(start, end + 1, 10):
    for j in range(0, 10):
        if i + j > end: break
        print(f'{i + j}: "{chr(i + j)}"', end=', ')

    print()

# ЗАДАЧА 2
#
# a – 40 + (8 + 24) * 15 = 520 bytes
# max_negative – 24 bytes
# position – 24 bytes
# i – 24 bytes
#
# суммарно 592 bytes

from random import randint
a = [randint(-20, 20) for _ in range(15)]
print(a)

max_negative = -float("inf")
position = None

for i in range(len(a)):
    if 0 > a[i] > max_negative:
        max_negative = a[i]
        position = i
print(f'a[{position}] = {max_negative}')