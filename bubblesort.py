import random
import copy
import unittest

def bubblesort(input):
    swapped = True
    while(swapped):
        swapped = False
        for i in range(0, len(input) - 1):
            if input[i] > input[i+1]:
                swapped = True
                input[i], input[i+1] = input[i+1], input[i]
    return input

class TestBubbleSort(unittest.TestCase):

    def test_upper(self):
        input = [random.randint(0, 100) for i in range(0, 100)]
        expectedOutput = copy.deepcopy(input)
        expectedOutput.sort()
        self.assertEqual(bubblesort(input), expectedOutput)

unittest.main()
