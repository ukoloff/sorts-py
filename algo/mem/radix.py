#
# Radix sort with arbitrary base
#

def sort(array, base=10):
    pos = [0] * base
    wrk = [[z, z, 0] for z in array]
    dup = wrk[:]
    while True:
        zero = True
        for i in range(base):
            pos[i] = 0
        for z in wrk:
            if z[1] != 0:
                zero = False
            z[2] = z[1] % base
            pos[z[2]] += 1
            z[1] //= base
        if zero:
            break
        ofs = 0
        for i, v in enumerate(pos):
            pos[i] = ofs
            ofs += v
        for z in wrk:
            dup[pos[z[2]]] = z
            pos[z[2]] += 1
        wrk, dup = dup, wrk
    for i, z in enumerate(wrk):
        array[i] = z[0]
