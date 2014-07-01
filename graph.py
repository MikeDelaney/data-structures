# -*- charset: utf-8 -*-


class Graph(object):
    def __init__(self):
        self.d = {}

    def nodes(self):
        return self.d.keys()

    def edges(self):
        return [(n, e) for n in self.d for e in self.d[n]]

    def add_node(self, node):
        if self.has_node(node):
            raise ValueError("Node already exists")
        self.d[node] = []

    def add_edge(self, node, endpoint):
        if not self.has_node(node):
            self.d[node] = []
        if not self.has_node(endpoint):
            self.d[endpoint] = []
        # there should not already be an edge from node to endpoint
        # and nodes cannot make an edge to themselves
        if endpoint not in self.d[node] and node != endpoint:
            self.d[node].append(endpoint)

    def del_node(self, node):
        if not self.has_node(node):
            raise ValueError
        del self.d[node]
        for endpoints in self.d.values():
            if node in endpoints:
                endpoints.remove(node)

    def has_node(self, node):
        return node in self.d

    def neighbors(self, node):
        if not self.has_node(node):
            raise ValueError
        return self.d[node]

    def adjacent(self, node, endpoint):
        if not self.has_node(node) or not self.has_node(endpoint):
            raise ValueError
        return endpoint in self.d[node]

    def depth_first(self, start):
        return self._traverse(start, 'depth')

    def breadth_first(self, start):
        return self._traverse(start, 'breadth')

    def _traverse(self, start, traversal):
        visited = []
        not_explored = [start]
        while not_explored:
            if traversal == 'depth':
                curr_node = not_explored.pop(0)
            else:
                curr_node = not_explored.pop()
            visited.append(curr_node)
            children = self.d[curr_node]
            if len(children) > 0:
                for child in children:
                    if child not in visited and child not in not_explored:
                        if traversal == 'depth':
                            not_explored.append(child)
                        else:
                            not_explored.insert(0, child)
        return visited
