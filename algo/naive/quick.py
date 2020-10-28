#
# Unoptimized Quick sort
#
from ..ins import sort as insort


def sort(array):
    if len(array) < 2:
      return
    x = pivot(array)
    lt = []
    eq = []
    gt = []
    for n in array:
      (eq if n == x else lt if n < x else gt).append(n)
    sort(lt)
    sort(gt)
    array[:] = lt + eq + gt


def pivot(array):
    three = [array[0], array[len(array) // 2], array[-1]]
    insort(three)
    return three[1]
