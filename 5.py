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
