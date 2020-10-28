#
# Non-optimized Merge sort
#


def sort(array):
    if len(array) < 2:
        return
    fence = len(array) // 2
    lft = array[:fence]
    sort(lft)
    rgt = array[fence:]
    sort(rgt)
    i = 0
    j = 0
    p = 0
    while True:
        if i >= len(lft):
            array[p:] = rgt[j:]
            break
        if j >= len(rgt):
            array[p:] = lft[i:]
            break
        if lft[i] < rgt[j]:
            array[p] = lft[i]
            i += 1
        else:
            array[p] = rgt[j]
            j += 1
        p += 1
