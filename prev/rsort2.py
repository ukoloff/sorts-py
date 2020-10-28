# Radix sort / binary
import numpy as np 
import tqdm

def rsort(arr):
  """
  Sort array of (unsigned) ints in place
  """

  def ones(bit):
    return sum(1 for item in arr if item & bit)

  def nonzero(bit):
    bit -= 1
    for item in arr:
      if item & bit != item:
        return True
    return False

  bit = 1
  while nonzero(bit):
    pos0 = 0
    pos1 = len(arr) - ones(bit)
    for item in arr[:]:
      if item & bit:
        arr[pos1] = item
        pos1 += 1
      else:
        arr[pos0] = item
        pos0 += 1
    bit <<= 1

for i in tqdm.trange(1000):
  a = list(map(int, np.random.randint(1, 54321, 500)))
  rsort(a)
  assert(a==sorted(a))
