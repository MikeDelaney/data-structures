# -*- charset: utf-8 -*-


class Graph(object):
    def __init__(self):
        self.d = {}

    def nodes(self):
        return self.d.keys()

    def edges(self):
        return [e for n in self.d for e in self.d[n]]

    def add_node(self, key):
        self.d[key] = []

    def add_edge(self, key1, key2):
        if key1 not in self.d:
            self.d[key1] = []
        if key2 not in self.d:
            self.d[key2] = []
        # there should not already be an edge from key1 to key2
        if key2 not in self.d[key1]:
            self.d[key1] = [key2]

    def del_node(self, key):
        if key not in self.d:
            raise ValueError
        del self.d[key]
        for edge in self.d.values():
            if key in edge:
                edge.remove(key)
