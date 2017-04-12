import random
import copy
import unittest

def quicksort(input):
    if not input or len(input) == 1:
        return input
    i = 0;
    for j in range(0, len(input) - 1):
        if input[j] <= input[-1]:
            input[i], input[j] = input[j], input[i]
            i+=1
    input.insert(i, input.pop(-1))
    return quicksort(input[0:i]) + [input[i]] + quicksort(input[i+1:])


class TestQuickSort2(unittest.TestCase):

    def test_upper(self):
        input = [random.randint(0, 100) for i in range(0, 100)]
        expectedOutput = copy.deepcopy(input)
        expectedOutput.sort()
        self.assertEqual(quicksort(input), expectedOutput)

unittest.main()