from random import randint
from time import time
import cProfile

a = [randint(-20, 20) for _ in range(10000000)]
start_time = time()


def main():
    max_negative = -float("inf")
    position = None
    for i in range(len(a)):
        if 0 > a[i] > max_negative:
            max_negative = a[i]
            position = i
    print(f'a[{position}] = {max_negative}')

main()
print(f'Time = {time() - start_time}')
# ‼️ Time = 1.3156168460845947
# cProfile.run('main()')
start_time = time()


def main_1():
    temp = map(lambda elem: float("-inf") if elem >= 0 else elem, a)
    max_negative = max(temp)
    print(f'a[{a.index(max_negative)}] = {max_negative}')


main_1()
print(f'Time = {time() - start_time}')
# ‼️ Time = 2.3767800331115723

