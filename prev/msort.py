import numpy as np 
import tqdm

def msort(arr):
  stride = 1
  while stride < len(arr):
    for i in range(0, len(arr) - stride, 2 * stride):
      eoB = min(len(arr), i + 2 * stride)
      eoA = i + stride
      posA = i
      posB = eoA
      result = []
      while posA < eoA and posB < eoB:
        if arr[posA] < arr[posB]:
          result.append(arr[posA])
          posA +=1
        else:
          result.append(arr[posB])
          posB +=1
      while posA < eoA:
        result.append(arr[posA])
        posA +=1
      while posB < eoB:
        result.append(arr[posB])
        posB +=1

      posA = i
      for item in result:
        arr[posA] = item
        posA += 1
    stride <<= 1


for i in tqdm.trange(1000):
  a = list(np.random.randint(1, 9, 500))
  msort(a)
  assert(a==sorted(a))
