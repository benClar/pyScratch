import random
import copy
import unittest


class Heap(object):

    def __init__(self):
        self._heap = []

    def add(self, d):
        self._heap.append(d)
        curr = len(self._heap) - 1
        while(self.hasParent(curr) and self.getParent(curr) < self._heap[curr]):
            self._heap[self.getParentIndex(curr)], self._heap[curr] = self._heap[curr], self._heap[self.getParentIndex(curr)]
            curr = self.getParentIndex(curr)

    def pop(self):
        ret = self._heap.pop(0)
        curr = 0
        while(self.hasLeftChild(curr)):
            largerChild = self.getLeftChildIndex(curr)
            if self.hasRightChild(curr) and self.getLeftChild(curr) < self.getRightChild(curr):
                largerChild = self.getRightChildIndex(curr)
            if self._heap[largerChild] > self._heap[curr]:
                self._heap[curr], self._heap[largerChild] = self._heap[largerChild], self._heap[curr]
            curr = largerChild
        return ret

    def getLeftChild(self, index):
        return self._heap[self.getLeftChildIndex(index)]

    def getRightChild(self, index):
        return self._heap[self.getRightChildIndex(index)]

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < len(self._heap)

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < len(self._heap)

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def getParent(self, index):
        return self._heap[self.getParentIndex(index)]

    def getRightChildIndex(self, index):
        return (2 * index) + 2

    def getLeftChildIndex(self, index):
        return (2 * index) + 1

    def getParentIndex(self, index):
        return (index - 1) / 2

class TestInsertionSort(unittest.TestCase):

    def test_upper(self):
        input = [random.randint(0, 100) for i in range(0, 100)]
        h = Heap()
        for i in [3, 5, 4, 10, 6, 78, 100, 50]:
            h.add(i)
        self.assertEqual(h.pop(), 100)
        self.assertEqual(h.pop(), 78)
        self.assertEqual(h.pop(), 50)
        self.assertEqual(h.pop(), 10)
        self.assertEqual(h.pop(), 6)
        self.assertEqual(h.pop(), 5)
        self.assertEqual(h.pop(), 4)
        self.assertEqual(h.pop(), 3)
unittest.main()