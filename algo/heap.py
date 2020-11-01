#
# Heap sort
#
import heapq


def sort(array):
    heap = array[:]
    heapq.heapify(heap)
    for i in range(len(array)):
        array[i] = heapq.heappop(heap)
