# -*- charset: utf-8 -*-


class Binheap(list):
    """
    Represents a binary heap as a list created from iterable. If no iterable,
    creates empty heap. minmax allows creation of max-heap and
    minheap objects.
    """
    def __init__(self, iterable=None, minmax="min"):
        if iterable is not None:
            self.extend(iterable)
        if minmax == "min":
            self.compare = self.comp_min
        else:
            self.compare = self.comp_max
        self._heapify()

    def comp_min(self, x, y):
        """
        Comparison for min-heap
        """
        return x < y

    def comp_max(self, x, y):
        """
        Comparison for max-heap
        """
        return x > y

    def _heapify(self):
        """
        Traverses levels of heap. Sends parent 'nodes' to _heapify.
        """
        for index in range(len(self)//2, -1, -1):
            self._heapify_sub(index)

    def _heapify_sub(self, index):
        """
        Heapifies a single subtree.
        """
        left = 2 * index + 1
        right = 2 * index + 2
        target = index
        if left < len(self):
            if self.compare(self[left], self[target]):
                target = left
        if right < len(self):
            if self.compare(self[right], self[target]):
                target = right
        if target != index:
            self[index], self[target] = (
                self[target], self[index])
            self._heapify_sub(target)

    def push(self, value):
        """
        Adds value to end of heap and heapifies the tree.
        """
        self.append(value)
        self._heapify()

    def pop(self):
        """
        Removes root of heap, replaces with last value, rebuilds tree.
        """
        self[0] = self[-1]
        super(Binheap, self).pop()
        self._heapify()
