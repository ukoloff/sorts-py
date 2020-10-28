#
# Bubble sort
#


def sort(array):
    for i in range(1, len(array) - 1):
        swapped = False
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            break
