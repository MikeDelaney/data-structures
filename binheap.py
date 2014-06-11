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

    def _heapify(self):
        # fix
        from pdb import set_trace
        #set_trace()
        for index in range(len(self)-1, 0, -1):
            parent = (index-1)//2
            if self.compare(self[index], self[parent]):
                self[index], self[parent] = self[parent], self[index]

    def push(self, value):
        pass

    def pop(self):
        pass
