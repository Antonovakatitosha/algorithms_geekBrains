from random import randint
a = [randint(0, 20) for _ in range(12)]
print(a)

first_min = float("inf")
second_min = float("inf")
for elem in a:
    if elem <= first_min:
        second_min = first_min
        first_min = elem
    elif elem <= second_min: second_min = elem

print(f"First min = {first_min}, second = {second_min}")
