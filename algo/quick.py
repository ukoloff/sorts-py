#
# Quick sort
#


def sort(array):
    if len(array) < 2:
        return
    x = pivot(array)
    lt = []
    eq = []
    gt = []
    for n in array:
        (eq if n == x else lt if n < x else gt).append(n)
    sort(lt)
    sort(gt)
    array[:] = lt + eq + gt


def pivot(array):
    three = [array[0], array[len(array) // 2], array[-1]]
    insort(three)
    return three[1]


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
