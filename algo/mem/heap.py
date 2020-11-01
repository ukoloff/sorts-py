#
# Heap sort
#

def sort(array):
    Heap(array).detach()


class Heap():
    """
    Implements Binary Heap over list
    """

    def __init__(self, array):
        self.data = array
        self.heapify()

    def top(self):
        return self.data[0]

    def empty(self):
        return self.fence == 0

    def heapify(self):
        self.fence = len(self.data)
        for i in range(self.fence // 2 - 1, -1, -1):
            self.siftDown(i)

    def detach_top(self):
        if self.fence == 0:
            return
        self.fence -= 1
        if self.fence == 0:
            return
        self.data[0], self.data[self.fence] = self.data[self.fence], self.data[0]
        self.siftDown()

    def detach(self):
        while self.fence > 0:
            self.detach_top()

    def siftUp(self, n=-1):
        n %= self.fence
        while n > 0:
            up = (n - 1) // 2
            if self.data[n] <= self.data[up]:
                break
            self.data[n], self.data[up] = self.data[up], self.data[n]
            n = up

    def siftDown(self, n=0):
        n %= self.fence
        while True:
            maxpos = n
            child = 2 * n
            for i in range(2):
                child += 1
                if child >= self.fence:
                    break
                if self.data[child] > self.data[maxpos]:
                    maxpos = child
            if maxpos == n:
                break
            self.data[n], self.data[maxpos] = self.data[maxpos], self.data[n]
            n = maxpos
