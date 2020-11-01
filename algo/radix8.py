#
# Radix sort by bytes
#

def sort(array):
    shift = 0
    unseen = 255
    while True:
        fragments = [[] for i in range(256)]
        empty = True
        for x in array:
            fragments[(x >> shift) & 255].append(x)
            if x & unseen != x:
                empty = False
        array[:] = sum(fragments, [])
        if empty:
            break
        shift += 8
        unseen = (unseen << 8) + 255
