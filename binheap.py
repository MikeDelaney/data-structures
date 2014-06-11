# -*- charset: utf-8 -*-


class binheap(list):
    def __init__(self, init=None, minmax="min"):
        if minmax == "min":
            self.compare = self.comp_min
        else:
            self.compare = self.comp_max

    def comp_min(self, x, y):
        pass

    def comp_max(self, x, y):
        pass

    def heapify(self):
        pass
