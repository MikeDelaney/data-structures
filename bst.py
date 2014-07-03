
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
            if self.right == None:
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
        pass

    def balance(self):
        pass
