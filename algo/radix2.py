#
# Radix sort bit by bit
#

def sort(array):
    bit = 1
    while True:
        v0 = []
        v1 = []
        empty = True
        mask = bit - 1 | bit
        for x in array:
            if x & mask != x:
                empty = False
            (v0 if x & bit == 0 else v1).append(x)
        array[:] = v0 + v1
        bit += bit
        if empty:
            break
