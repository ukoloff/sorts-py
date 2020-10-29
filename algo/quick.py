#
# Quick sort
#

def sort(array):

    three = [0] * 3

    def pivot(l, h):
        three[0] = array[l]
        three[1] = array[(l + h) // 2]
        three[2] = array[h]
        insort(three)
        return three[1]

    def sort(l, h):
        if l >= h:
            return
        pivo = pivot(l, h)
        lo, hi = l, h
        while lo <= hi:
            while array[lo] < pivo:
                lo += 1
            while array[hi] > pivo:
                hi -= 1
            if lo >= hi:
                break
            array[lo], array[hi] = array[hi], array[lo]
            lo += 1
            hi -= 1
        sort(l, hi)
        sort(hi+1, h)

    sort(0, len(array)-1)


def insort(array):
    """
    Insertion sort
    """
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and array[j - 1] > item:
            array[j] = array[j - 1]
            j -= 1
        if i != j:
            array[j] = item
