import time
from .algo import enum
from .samples import of


def run():
    fns = enum()
    print(batch_times(fns['bubble'].sort))

def validate(fn, samples):
  for data in samples:
    a = data[:]
    b = data[:]
    fn(a)
    b.sort()
    assert(a == b)

def single_time(fn, samples, cycles=10):
  start = time.time()
  for data in samples:
    for i in range(cycles):
      a = data[:]
      fn(a)
  stop = time.time()
  return (stop - start) / cycles / len(samples)

def batch_times(fn, max=30):
  start = time.time()
  result = {}
  size = 1
  while True:
    data = of(size)
    result[size] = single_time(fn, data)
    now = time.time()
    if now - start > max:
      break
    size *= 2
  return result

run()
