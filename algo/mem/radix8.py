#
# Radix sort by bytes
#

def sort(array):
    tmp = array[:]
    pos = [0] * 256
    unseen = 0
    shift = 0
    while True:
        for i in range(256):
            pos[i] = 0
        zero = True
        for x in array:
            if x & unseen != x:
                zero = False
            pos[(x >> shift) & 255] += 1
        if zero:
            break
        ofs = 0
        for i, v in enumerate(pos):
            pos[i] = ofs
            ofs += v
        for x in array:
            idx = (x >> shift) & 255
            tmp[pos[idx]] = x
            pos[idx] += 1
        array[:] = tmp
        shift += 8
        unseen = (unseen << 8) + 255
