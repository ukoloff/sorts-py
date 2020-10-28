#
# Insertion sort
#


def sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i
        while j > 0 and array[j - 1] > item:
            array[j] = array[j - 1]
            j -= 1
        if i != j:
            array[j] = item
