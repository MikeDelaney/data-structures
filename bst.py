
class BSTree(object):
    def __init__(self, key=None, root=None):
        self.key = key
        self.root = root
        self.left = None
        self.right = float('inf')

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
            if self.right == float('inf'):
                self.right = BSTree()
            self.right.insert(key)


    def size(self):
        pass

    def depth(self):
        pass

    def balance(self):
        pass
