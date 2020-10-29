#
# Selection sort
#

def sort(array):
    for i in range(len(array)):
        minpos = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minpos]:
                minpos = j
        if i != minpos:
            array[i], array[minpos] = array[minpos], array[i]
