#
# Quick sort
#

def sort(array):

    three = [0] * 3

    def partition(l, h, pivot):
        while l <= h:
            while array[l] < pivot:
                l += 1
            while array[h] > pivot:
                h -= 1
            if l >= h:
                break
            array[l], array[h] = array[h], array[l]
            l += 1
            h -= 1
        return h

    def pivot(l, h):
        three[0] = array[l]
        three[1] = array[(l + h) // 2]
        three[2] = array[h]
        insort(three)
        return three[1]

    def sort(l, h):
        if l >= h:
            return
        i = partition(l, h, pivot(l, h))
        sort(l, i)
        sort(i+1, h)

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
