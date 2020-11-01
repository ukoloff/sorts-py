#
# Shell sort
#
# https://www.alphacodingskills.com/python/pages/python-program-for-shell-sort.php
#

def sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j -= gap
            array[j] = temp
        gap = gap // 2
