import time
from .algo import enum
from .samples import generate


def run():
    data = generate()
    for name, module in enum().items():
        print(name, end='\t')
        start = time.time()
        for array in data:
            print('.', end='', flush=True)
            a = array[:]
            module.sort(a)
            b = array[:]
            b.sort()
            assert a == b, f"Mismatch for {name} @{array}"
        stop = time.time()
        print('', stop - start)

run()
