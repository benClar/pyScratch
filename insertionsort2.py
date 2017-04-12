import random
import copy
import unittest


def insertionSort(input, sorted=0):
    insertion = True
    while(insertion):
        insertion = False
        for i in range(sorted, len(input)):
            for j in range(0, sorted+1):
                if input[i] <= input[j]:
                    input.insert(j, input.pop(i))
                    sorted += 1
                    insertion = True
                    break
            if insertion:
                break
    return input



class TestInsertionSort(unittest.TestCase):

    def test_upper(self):
        input = [random.randint(0, 100) for i in range(0, 1000)]
        expectedOutput = copy.deepcopy(input)
        expectedOutput.sort()
        self.assertEqual(insertionSort(input), expectedOutput)

print insertionSort([9,7,5,8,3,10,4])