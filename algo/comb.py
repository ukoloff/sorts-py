#
# Comb sort
#
# https://www.geeksforgeeks.org/python-program-for-comb-sort/
#

def sort(array):
    n = len(array)
    gap = n
    swapped = True

    while gap != 1 or swapped:
        gap = max(1, gap * 10 // 13)
        swapped = False
        for i in range(0, n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
