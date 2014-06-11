# -*- charset: utf-8 -*-


class binheap(list):
    def comp_min(self, x, y):
        pass

    def comp_max(self, x, y):
        pass

    def __init(self, init, minmax="min"):
        if minmax == "min":
            self.compare = binheap.comp_min
        else:
            self.compare = binheap.comp_max

    def heapify(self):
        pass
