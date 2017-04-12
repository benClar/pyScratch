import random
import copy
import unittest
from itertools import chain

def mergesort(input):
    odd = None
    if len(input) == 1:
        return input
    if len(input)%2:
        odd = input.pop(-1)
    pairs = [(input[i], input[i+1]) for i in range(0, len(input), 2)]
    mergedPairs = [merge(*pair) for pair in pairs]
    if odd:
        mergedPairs.append(merge(mergedPairs.pop(-1), odd))
    return mergesort(mergedPairs)

def merge(a, b):
    merged = []
    while(a or b):
        if not b or (a and a[0] <= b[0]):
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    return merged

class TestMergeSort(unittest.TestCase):

    def test_mergeSort(self):
        input = [random.randint(0, 100) for i in range(0, 100)]
        expectedOutput = copy.deepcopy(input)
        expectedOutput.sort()
        self.assertEqual(list(chain(*mergesort([[i] for i in input]))), expectedOutput)

unittest.main()

# print list(chain(*mergesort([[i] for i in [4,3,6,2,7,8,10,1]])))