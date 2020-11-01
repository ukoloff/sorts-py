#
# Radix sort with arbitrary base
#

def sort(array, base=10):
    wrk = [[z, z] for z in array]
    while True:
        empty = True
        fragments = [[] for i in range(base)]
        for z in wrk:
            fragments[z[1] % base].append(z)
            z[1] //= base
            if z[1] != 0:
              empty = False
        wrk[:] = sum(fragments, [])
        if empty:
            break
    for i, z in enumerate(wrk):
        array[i] = z[0]
