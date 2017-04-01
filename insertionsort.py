import random
import copy
import unittest


def insertionSort(input):
    sortedB = 1
    for unsortedElement in range(1, len(input)):
        curr = input[unsortedElement]
        sortedElements = reversed(range(0, sortedB + 1))
        for sortedElement in sortedElements:
            if not sortedElement:
                input[sortedElement] = curr
            elif curr < input[sortedElement - 1]:
                input[sortedElement] = input[sortedElement - 1]
            else:
                input[sortedElement] = curr
                break
        sortedB += 1
    return input


class TestInsertionSort(unittest.TestCase):

    def test_upper(self):
        input = [random.randint(0, 100) for i in range(0, 100)]
        expectedOutput = copy.deepcopy(input)
        expectedOutput.sort()
        self.assertEqual(insertionSort(input), expectedOutput)

unittest.main()
