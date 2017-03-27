import random
import copy
import unittest

def quickSort(input):
    if len(input) == 1 or not input:
        return input
    i = 0
    swapped = True
    while(swapped and i != len(input)-1):
        swapped = False
        for j in range(i, len(input)):
            if input[-1] >= input[j]:
                swapped = True
                input[i], input[j] = input[j], input[i]
                i+=1
                break
    input.insert(i, input.pop(-1))
    return quickSort(input[0:i]) + quickSort(input[i:])


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        input = [random.randint(0, 100) for i in range(0, 100)]
        expectedOutput = copy.deepcopy(input)
        expectedOutput.sort()
        self.assertEqual(quickSort(input), expectedOutput)

unittest.main()