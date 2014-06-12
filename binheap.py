# -*- charset: utf-8 -*-


class Binheap(object):
    """
    Represents a binary heap as a list created from iterable. If no iterable,
    creates empty heap. minmax allows creation of max-heap and
    minheap objects.
    """
    def __init__(self, iterable=None, minmax="min"):
        if iterable is not None:
            self._list = list(iterable)
        else:
            self._list = []
        if minmax == "min":
            self.minmax = "min"
            self.compare = self.comp_min
        else:
            self.minmax = "max"
            self.compare = self.comp_max
        self._build()

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

    def _build(self):
        """
        Traverses levels of heap. Sends parent 'nodes' to _heapify.
        """
        for index in range(len(self._list)//2, -1, -1):
            self._heapify(index)

    def _heapify(self, index):
        """
        Heapifies a single subtree.
        """
        left = 2 * index + 1
        right = 2 * index + 2
        target = index
        if left <= len(self._list)-1:
            if self.compare(self._list[left], self._list[target]):
                target = left
        if right <= len(self._list)-1:
            if self.compare(self._list[right], self._list[target]):
                target = right
        if target != index:
            self._list[index], self._list[target] = (
                self._list[target], self._list[index])
            self._heapify(target)

    def push(self, value):
        """
        Adds value to end of heap and heapifies the tree.
        """
        self._list.append(value)
        self._build()

    def pop(self):
        """
        Removes root of heap, replaces with last value, rebuilds tree.
        """
        last = self._list.pop()
        copy = self._list[1:]
        copy.insert(0, last)
        temp = Binheap(copy, self.minmax)
        self._list = temp._list
