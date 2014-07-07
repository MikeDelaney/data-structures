[![Build Status](https://travis-ci.org/MikeDelaney/data-structures.svg?branch=master)](https://travis-ci.org/MikeDelaney/data-structures)

data-structures
===============

Sample code for a number of classic data structures.

##Authors
* Jonathan Siebert
* Mike Delaney

##Singly linked list - linked_list.py

##Stack - stack.py

##Queue - queue.py

##Doubly linked list - dll.py
Used http://python.dzone.com/articles/algorithm-week-linked-list as a guide for simplifying code in remove function.
Got an idea for a doubly linked list use case from https://community.oracle.com/message/10431517#10431517

As singly linked list might be appropriate as the basis of a stack, and a doubly linked list might be useful to keep a record of commands for undo/redo.

##Binary Heap - binheap.py

##Priority Queue - priorityq.py

##Simple parenthesis counter - parenthetics.py

##Simple Graph - graph.py

An implementation of a weighted directional graph.
Has methods for:
* adding nodes
* deleting nodes
* returning a list of nodes
* returning a list of a node's neighbors
* determining if nodes are adjacent
* adding edges
* returning a list of edges with weights
* returning complete traversals, either depth-first or breadth-first.
* determining the shortest path between nodes using either Dijkstra's algorithm or the Bellman-Ford algoritm.

The implementation of Dijkstra's used here works by finding the shortest distance from a start node to every other node in the graph. Initially all distances are assumed to be infinite. The algorithm then determines the actual distances to neighboring nodes and expands outwards in order of closeness. Once all distances are known, the shortest path is determined by backtracking from the end to the start through previous nodes. Dijkstra's is faster than Bellman-Ford, but does not work for graphs with negative weights.

The Bellman-Ford algorithm starts with the same assumptions as Dijkstra's.  Bellman-Ford differs primarily in that it iterates over all of the edges when determining actual distances instead of selecting the closest. Once all of the distances are known, the same backtracking method is used to get the shortest path. The Bellman-Ford algorithm is slower, but works for graphs with negative weights. If negative weight cycles exist, an error is raised.

Based the implementation of both algorithms on their Wikipedia entries and pseudocode. See [Dijkstra's](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) and [Bellman-Ford](http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) for more information.

##Binary Search Tree - bst.py

Class based implementation of a binary search tree with the following methods:
* insert(val)
* contains(val)
* size()
* depth()
* balance()
* in-order traversal
* pre-order traversal
* post-order traversal
* breadth-first traversal

Includes code to produce dot object for graphviz visualization program.

Algorithms for traversal based on [this](http://en.wikipedia.org/wiki/Pre-order_traversal) Wikipedia article.