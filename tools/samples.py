import random


def generate():
    manual = """
    3 14 159 2 6 5 35
    42 9 17 54 602 3 54 999 11
    """.rstrip().splitlines()
    result = [[int(z) for z in line.split()] for line in manual]

    for i in range(12):
        size = 1 << i
        result.extend([
            [1] * size,
            [size + 1] * size,
            list(range(size)),
            list(range(size, 0, -1)),
            *[[random.randrange(10 ** (z + 5)) for i in range(size)] for z in range(3)]
        ])
    for fn in [sorted, reversed]:
        result.extend(list(map(lambda z: list(fn(z)), result)))
    random.shuffle(result)
    return result
