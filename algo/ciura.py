#
# Shell sort with Ciura sequence
#
# https://en.wikipedia.org/wiki/Shellsort
# https://oeis.org/A102549
# https://www.alphacodingskills.com/python/pages/python-program-for-shell-sort.php
#

ciura = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

def sort(array):
    n = len(array)

    while ciura[-1] < n:
      ciura.append((ciura[-1] * 9 + 7) // 4)
    cidx = 0
    while ciura[cidx] < n:
      cidx += 1
    for gap in reversed(ciura[:cidx]):
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j -= gap
            array[j] = temp
