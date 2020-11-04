import random


def generate():
    manual = """
    3 14 159 2 6 5 35
    42 9 17 54 602 3 54 999 11
    """.rstrip().splitlines()
    result = [[int(z) for z in line.split()] for line in manual]

    for i in range(12):
        size = 1 << i
        size = random.randint(size - size // 4, size + size // 4)
        result.extend([
            [1] * size,
            [size + 1] * size,
            list(range(size)),
            list(range(size, 0, -1)),
            *triplicate([
                [random.randrange(10 ** (base + 1)) for i in range(size)]
                for base in range(6)])
        ])
    random.shuffle(result)
    return result


def triplicate(samples):
    """
    Add sorted versions of samples
    """
    asc = [sorted(z) for z in samples]
    desc = [list(reversed(z)) for z in asc]
    return samples + asc + desc


def of(size):
    return [
        [1] * size,
        [size + 1] * size,
        list(range(size)),
        list(range(size, 0, -1)),
        *triplicate([
            [random.randrange(10 ** (base + 1)) for i in range(size)]
            for base in range(6)])
    ]
