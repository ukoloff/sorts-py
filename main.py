import tools.algo
import tools.samples


def run():
    data = tools.samples.generate()
    for name, module in tools.algo.enum().items():
        print(name, end='\t')
        for array in data:
            print('.', end='', flush=True)
            a = array[:]
            module.sort(a)
            b = array[:]
            b.sort()
            assert a == b, f"Mismatch for {name} @{array}"
        print()

run()
