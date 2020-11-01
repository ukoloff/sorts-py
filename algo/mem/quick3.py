#
# Quick sort with triple split
#

def sort(array):

    three = [0] * 3

    def pivot(l, h):
        three[0] = array[l]
        three[1] = array[(l + h) // 2]
        three[2] = array[h]
        insort(three)
        return three[1]

    def partition(l, h, pivot):
        eq = l
        gt = h + 1
        here = l
        while here < gt:
            if array[here] == pivot:
                here += 1
                continue
            if array[here] < pivot:
                if eq != here:
                    array[here], array[eq] = array[eq], array[here]
                eq += 1
                here += 1
                continue
            # array[here] > pivot
            while True:
                gt -= 1
                if gt <= here:
                    break
                if array[gt] <= pivot:
                    array[gt], array[here] = array[here], array[gt]
                    break
        return (eq, gt)

    def sort(l, h):
        if l >= h:
            return
        eq, gt = partition(l, h, pivot(l, h))
        sort(l, eq)
        sort(gt, h)

    sort(0, len(array) - 1)


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
