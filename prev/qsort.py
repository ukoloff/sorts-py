# https://habr.com/sandbox/29775/
import numpy as np 
import tqdm

def qsort(arr):

    def partition(arr, l, h, pivot):
        while l <= h:
            while arr[l] < pivot:
                l += 1
            while arr[h] > pivot:
                h -= 1
            if l >= h:
                break
            t = a[l]
            a[l] = a[h]
            a[h] = t
            l += 1
            h -= 1
        return h

    def sort(arr, l, h):
        if l >= h:
            return
        i = partition(arr, l, h, arr[(l+h)//2])
        sort(arr, l, i)
        sort(arr, i+1, h)

    sort(arr, 0, len(arr)-1)

for i in tqdm.trange(1000):
    a = list(np.random.randint(1, 9, 500))
    qsort(a)
    assert(a==sorted(a))

