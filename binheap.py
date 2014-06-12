# -*- charset: utf-8 -*-


class binheap(list):
    def __init__(self, init=None, minmax="min"):
        if minmax == "min":
            self.compare = self.comp_min
        else:
            self.compare = self.comp_max
        if init is not None:
            self.extend(init)
            self._heapify()

    def comp_min(self, x, y):
        return x < y

    def comp_max(self, x, y):
        return x > y

    def _build(self):
        for index in range(len(self)//2, -1, -1):
            self._heapify(index)

    def _heapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        target = index
        if left <= len(self)-1 and self.compare(self[left], self[target]):
            target = left
        if right <= len(self)-1 and self.compare(self[right], self[target]):
                target = right
        if target != index:
            self[index], self[target] = self[target], self[index]
            self._heapify(target)

    def push(self, value):
        pass

    def pop(self):
        pass
