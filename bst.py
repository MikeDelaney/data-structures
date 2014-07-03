
class BSTree(object):
    def __init__(self, key=None, root=None):
        self.key = key
        self.root = root
        self.left = None
        self.right = None

    def insert(self, key):
        if key == self.key:
            return
        elif self.key is None:
            self.key = key
        elif key < self.key:
            if self.left is None:
                self.left = BSTree()
            self.left.insert(key)
        else:
            if self.right is None:
                self.right = BSTree()
            self.right.insert(key)

    def contains(self, key):
        if key == self.key:
            return True
        elif self.key is None:
            return False
        elif key < self.key:
            if not self.left:
                return False
            return self.left.contains(key)
        else:
            if not self.right:
                return False
            return self.right.contains(key)

    def size(self):
        left_size = 0
        right_size = 0
        if self.left is not None:
            left_size = self.left.size()
        if self.right is not None:
            right_size = self.right.size()
        return 1 + left_size + right_size

    def depth(self):
        left_depth = 0
        right_depth = 0
        if self.left is not None:
            left_depth = self.left.depth()
        if self.right is not None:
            right_depth = self.right.depth()
        return 1 + max(left_depth, right_depth)

    def balance(self):
        return self.left.size() - self.right.size()


if __name__ == '__main__':
    import time
    # largest number of recursions we can get
    num = 996
    tree = BSTree()
    for i in range(num):
        tree.insert(i)

    print
    print 'Searching in degenerate BST of length {}'.format(num)
    print
    print 'Root:'

    # best case
    start = time.time()
    tree.contains(1)
    delta = time.time() - start
    print "Best case time = {}ns".format(delta * 1000)

    print
    print 'Leaf:'

    start = time.time()
    tree.contains(num - 1)
    delta = time.time() - start
    print "Worst case time = {}ns".format(delta * 1000)
