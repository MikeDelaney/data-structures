import random
from queue import Queue, Node


class BSTree(object):
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, key):
        if not self.key:
            self.key = key
        elif key < self.key:
            if not self.left:
                self.left = BSTree(None, self)
            self.left.insert(key)
        elif key > self.key:
            if not self.right:
                self.right = BSTree(None, self)
            self.right.insert(key)

    def contains(self, key):
        if key == self.key:
            return True
        elif key < self.key:
            if not self.left:
                return False
            return self.left.contains(key)
        else:
            if not self.right:
                return False
            return self.right.contains(key)

    def size(self):
        left_size, right_size = 0, 0
        if self.left:
            left_size = self.left.size()
        if self.right:
            right_size = self.right.size()
        return 1 + left_size + right_size

    def depth(self):
        left_depth, right_depth = 0, 0
        if self.left:
            left_depth = self.left.depth()
        if self.right:
            right_depth = self.right.depth()
        return 1 + max(left_depth, right_depth)

    def balance(self):
        return self.left.depth() - self.right.depth()

    def in_order(self):
        if self is not None:
            if self.left:
                for node in self.left.in_order():
                    yield node
            yield self
            if self.right:
                for node in self.right.in_order():
                    yield node

    def pre_order(self):
        if self is not None:
            yield self
            if self.left:
                for node in self.left.pre_order():
                    yield node
            if self.right:
                for node in self.right.pre_order():
                    yield node

    def post_order(self):
        if self is not None:
            if self.left:
                for node in self.left.post_order():
                    yield node
            if self.right:
                for node in self.right.post_order():
                    yield node
            yield self

    def breadth_first(self):
        visited = Queue()
        visited.enqueue(self)
        while visited:
            try:
                node = visited.dequeue()
            except LookupError:
                return
            if node.left:
                visited.enqueue(node.left)
            if node.right:
                visited.enqueue(node.right)
            yield node

    def delete(self, value):
        node_list = [node for node in self.in_order()]
        for i in xrange(len(node_list)):
            check = node_list[i]
            if check.key == value:
                children = check._number_children()
                if children == 0:
                    check._delete_leaf()
                elif children == 1:
                    check._delete_one_child()
                else:
                    check._delete_two_children(i, node_list)
        pass

    def _number_children(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def _delete_leaf(self):
        if self.parent.left == self:
            self.parent.left = None
        else:
            self.parent.right = None

    def _delete_one_child(self):
        if self.left:
            self.left.parent = self.parent
            self.parent.left = self.left
            self.left = None
        else:
            self.right.parent = self.parent
            self.parent.right = self.right
            self.right = None

    def _delete_two_children(self, i, node_list):
        if self.balance() > 0:
            self.key = node_list[i-1].key
            self.left.delete(self.key)
        else:
            self.key = node_list[i+1].key
            self.right.delete(self.key)

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.key is None else (
            "\t%s;\n%s\n" % (
                self.key,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.key, self.left.key)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.key, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.key, self.right.key)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.key, r)


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

    # tree = BSTree(4)
    # tree.insert(2)
    # tree.insert(6)
    # tree.insert(1)
    # tree.insert(3)
    # tree.insert(5)
    # tree.insert(7)
    # tree.insert(8)
    # tree.insert(0)
    # print tree.get_dot()
