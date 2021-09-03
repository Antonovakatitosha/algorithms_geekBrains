signs = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def convert_sign(sign):
    if sign in signs: return signs[sign]
    return int(sign)


def convert_to_sign(number):
    if number >= 10:
        for key, value in signs.items():
            if value == number: return key
    return str(number)


a = ['A', '2']
b = ['C', '4', 'F']
print(f'a = {"".join(a)}, b = {"".join(b)}')


a = [convert_sign(i) for i in a]
b = [convert_sign(i) for i in b]


def add_hex(first, second):
    second = second.copy()
    first = first.copy()

    if len(second) > len(first):
        first, second = second, first
    first = [0] + first
    remember = False
    for pos in range(len(first) - 1, -1, -1):
        to_add = 1 if remember else 0

        if len(second): to_add += second.pop()
        first[pos] = first[pos] + to_add

        if first[pos] >= 16:
            remember = True
            first[pos] -= 16
        else: remember = False

    return [convert_to_sign(number) for number in first]


def product(first, second):
    if len(second) > len(first):
        first, second = second, first
    matrix = [[0 for _ in range(len(first) + 2)] for _ in range(len(second))]

    for i, num_1 in enumerate(second[::-1]):
        # print(f'second[{i}] = {num_1}')

        remember = 0
        for j, num_2 in enumerate(first[::-1] + [0]):
            elem = num_2 * num_1 + remember

            if elem >= 16:
                remember = elem // 16
                elem = elem % 16
            else:
                remember = 0
            matrix[i][len(matrix[0]) - i - j - 1] = elem

    result = []
    remember = 0
    for i in list(zip(*matrix))[::-1]:
        elem = sum(i) + remember
        if elem > 15:
            remember = 1
            elem -= 16
        else: remember = 0
        result.append(elem)

    return [convert_to_sign(number) for number in result[::-1]]


print("sum =", "".join(add_hex(b, a)))
print("product =", "".join(product(a, b)))
# sum = 0CF1
# product = 7C9FE

