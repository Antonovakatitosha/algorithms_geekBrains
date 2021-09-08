from random import randint
from functools import reduce

a = [[randint(0, 9) for _ in range(4)] for _ in range(4)]
print(a)
print("Result:",
      reduce(lambda a, b: a if a > b else b,
             map(lambda line: reduce(lambda a, b: a if a < b else b, line, float("inf")), a), -float("inf")))
