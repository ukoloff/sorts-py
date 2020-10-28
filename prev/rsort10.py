# Radix sort / decimal
import numpy as np 
import tqdm

class Triple:
  """
  Helper class for Decimal Radix Sort
  """

  BASE = 10

  def __init__(self, n):
    self.n = n
    self.quot = n
    self.rem = 0

  def divide(self):
    z = self.quot
    self.quot = z // self.BASE
    self.rem = z % self.BASE

  def __repr__(self):
    return "<{}:{}/{}>".format(self.n, self.quot, self.rem)

def rsort(arr):
  triples = [Triple(item) for item in arr]

  while any(z.quot for z in triples):
    counts = [0] * Triple.BASE
    for z in triples:
      z.divide()
      counts[z.rem] += 1

    pos = 0
    for i, cnt in enumerate(counts):
      pos, counts[i] = pos + cnt, pos

    for z in triples[:]:
      triples[counts[z.rem]] = z
      counts[z.rem] += 1

  for i, z in enumerate(triples):
    arr[i] = z.n

for i in tqdm.trange(1000):
  a = list(map(int, np.random.randint(1, 54321, 500)))
  rsort(a)
  assert(a==sorted(a))
