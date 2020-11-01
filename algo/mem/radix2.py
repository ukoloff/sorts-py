#
# Radix sort bit by bit
#

def sort(array):
    tmp = array[:]
    bit = 1

    def empty():
        mask = bit - 1
        for x in array:
            if x & mask != x:
                return False
        return True

    while not empty():
        pos0 = 0
        pos1 = sum(1 for x in array if x & bit == 0)
        for x in array:
            if x & bit == 0:
                tmp[pos0] = x
                pos0 += 1
            else:
                tmp[pos1] = x
                pos1 += 1
        array[:] = tmp
        bit += bit
