# -*- charset: utf-8 -*-


class Graph(dict):
    def __init__(self):
        self.d = {}

    def nodes(self):
        return self.d.keys()

    def edges(self):
        return [e for n in self.d for e in self.d[n]]

    def add_node(self, key):
        self.d[key] = []
