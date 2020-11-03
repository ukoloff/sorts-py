import time
import random
from pathlib import Path
from .algo import enum


def run():
    mods = enum()
    for name, mod in mods.items():
      fn = mod.sort
      times = batch_times(fn)
      logs = Path(__file__).parent.parent / "log"
      logs.mkdir(parents=True, exist_ok=True)
      with (logs / (name + ".txt")).open("w") as f:
        for k, v in times.items():
          print(k, v, file=f)
        print(times, file=f)

def of(size):
    return [
        [1] * size,
        list(range(size)),
        list(range(size, 0, -1)),
        *[
            [random.randrange(10 ** (base + 1)) for i in range(size)]
            for base in range(5)]
    ]

def validate(fn, samples):
  for data in samples:
    a = data[:]
    b = data[:]
    fn(a)
    b.sort()
    assert(a == b)

def single_time(fn, samples, cycles=10):
  start = time.perf_counter()
  for data in samples:
    for i in range(cycles):
      a = data[:]
      fn(a)
  stop = time.perf_counter()
  return (stop - start) / cycles / len(samples)

def batch_times(fn, max=60):
  start = time.time()
  result = {}
  size = 1
  shown = False
  while True:
    data = of(size)
    validate(fn, data)
    result[size] = single_time(fn, data)
    now = time.time()
    elapsed = round(now - start)
    if elapsed != shown:
      print("\r" , fn.__module__, "\t", elapsed, end="", sep='')
      shown = elapsed
    if now - start > max:
      break
    size *= 2
  print()
  return result

run()
