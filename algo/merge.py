#
# Merge sort
#

def sort(array):

    tmp = array[:]

    stride = 1
    while stride < len(array):
        for i in range(0, len(array) - stride, 2 * stride):
            eoB = min(len(array), i + 2 * stride)
            eoA = i + stride
            posA = i
            posB = eoA
            posT = i
            while True:
                if posA >= eoA:
                    tmp[posT:eoB] = array[posB:eoB]
                    break
                if posB >= eoB:
                    tmp[posT:eoB] = array[posA:eoA]
                    break
                if array[posA] > array[posB]:
                    tmp[posT] = array[posB]
                    posB += 1
                else:
                    tmp[posT] = array[posA]
                    posA += 1
                posT += 1
            array[i:eoB] = tmp[i:eoB]
        stride += stride
