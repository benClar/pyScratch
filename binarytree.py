import unittest

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, node):
        if self.left is None:
            self.left = node
        else:
            self.right = node

class Tree(object):

    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root is None:
            self.root = node
            return
        self._add(self.root, node)

    def _add(self, currentNode, newNode):
        if newNode.data < currentNode.data:
            if currentNode.left is None:
                currentNode.left = newNode
            else:
                self._add(currentNode.left, newNode)
        else:
            if currentNode.right is None:
                currentNode.right = newNode
            else:
                self._add(currentNode.right, newNode)

    def getBreadthFirst(self):
        queue = [self.root]
        data = []
        return self._visitBreadFirst(data, queue)

    def getDepthFirst(self):
        data = []
        return self._visitDepthFirst(self.root, data)

    def _visitDepthFirst(self, current, data):
        data.append(current.data)
        if current.left:
            self._visitDepthFirst(current.left, data)
        if current.right:
            self._visitDepthFirst(current.right, data)
        return data

    def _visitBreadFirst(self, data, queue):
        if not queue:
            return data
        curr = queue.pop(0)
        data.append(curr.data)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        return self._visitBreadFirst(data, queue)

class TestTree(unittest.TestCase):

    def test_breadthFirst(self):
        t = Tree()
        d = [5, 7, 2, 6, 8, 3, 4]
        for i in d:
            t.add(Node(i))
        self.assertEqual(t.getBreadthFirst(), [5, 2, 7, 3, 6, 8, 4])


    def test_depthFirst(self):
        t = Tree()
        d = [5, 7, 2, 6, 8, 3, 4]
        for i in d:
            t.add(Node(i))
        self.assertEqual(t.getDepthFirst(), [5, 2, 3, 4, 7, 6, 8])

unittest.main()