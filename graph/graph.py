# -*- charset: utf-8 -*-


class Graph(object):
    def __init__(self):
        self.d = {}

    def nodes(self):
        return self.d.keys()

    def edges(self):
        return [(n, e, self.d[n][e]) for n in self.d for e in self.d[n]]

    def add_node(self, node):
        if self.has_node(node):
            raise ValueError("Node already exists")
        self.d[node] = {}

    def add_edge(self, node, endpoint, weight):
        if not self.has_node(node):
            self.d[node] = {}
        if not self.has_node(endpoint):
            self.d[endpoint] = {}
        # there should not already be an edge from node to endpoint
        # and nodes cannot make an edge to themselves
        if endpoint not in self.d[node] and node != endpoint:
            self.d[node][endpoint] = weight

    def del_node(self, node):
        del self.d[node]
        for nodes in self.d:
            if node in self.d[nodes]:
                del self.d[nodes][node]

    def has_node(self, node):
        return node in self.d

    def neighbors(self, node):
        return sorted(self.d[node].keys())

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
            if children:
                for child in children:
                    if child not in visited and child not in not_explored:
                        if traversal == 'depth':
                            not_explored.append(child)
                        else:
                            not_explored.insert(0, child)
        return visited

    def dijkstra(self, start, end):
        # Implementation is based on pseudocode from wikipedia
        dist, prev, nodes = self._algorithm_setup(start)
        # While list of nodes is not empty
        while nodes:
            # Find the node in nodes with the min distance
            closest_node = None
            for node in nodes:
                if node in dist:
                    if closest_node is None or dist[node] < dist[closest_node]:
                        closest_node = node
            # Exit condition if there is no closest node
            if closest_node is None:
                break
            # Remove closest_node from list
            nodes.remove(closest_node)
            # Iterate through neighbors of closest_node
            # Add the node with shortest path to dist
            for neighbor in self.neighbors(closest_node):
                path_length = dist[closest_node] + \
                    self.d[closest_node][neighbor]
                if path_length < dist[neighbor]:
                    dist[neighbor] = path_length
                    prev[neighbor] = closest_node
        return self._build_shortest_path(end, prev)

    def bellman_ford(self, start, end):
        dist, prev, nodes = self._algorithm_setup(start)
        # Relax edges
        for i in xrange(1, len(nodes)):
            # edge is (start_node, end_node, weight)
            for edge in self.edges():
                if dist[edge[0]] + edge[2] < dist[edge[1]]:
                    dist[edge[1]] = dist[edge[0]] + edge[2]
                    prev[edge[1]] = edge[0]
        # Check for negative cycles
        for edge in self.edges():
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                raise Exception('Graph contains negative weight cycle')
        return self._build_shortest_path(end, prev)

    def _algorithm_setup(self, start):
        # dist maps node to distance
        dist = {start: 0}
        # prev maps node to previous node
        prev = {start: None}
        # Get list of nodes
        nodes = self.nodes()
        # Iterate through nodes, add to dist with infinite distance and
        # None for previous node
        for node in nodes:
            if node != start:
                dist[node] = float('inf')
                prev[node] = None
        return dist, prev, nodes

    def _build_shortest_path(self, end, prev):
        # Backtrack from end through previous nodes to get path
        shortest_path = [end]
        while prev[end] is not None:
            shortest_path.insert(0, prev[end])
            end = prev[end]
        return shortest_path
