# -*- charset: utf-8 -*-

import pytest
from graph import Graph


@pytest.fixture(scope="function")
def simple_graph():
    graph = Graph()
    graph.d = {'A': {'B': 1},
               'B': {}}
    return graph


@pytest.fixture(scope="function")
def simple_non_cylic():
    graph = Graph()
    graph.d = {'A': {'B': 1, 'C': 2},
               'B': {},
               'C': {'D': 3, 'E': 5},
               'D': {},
               'E': {}}
    return graph


@pytest.fixture(scope="function")
def simple_cyclic():
    graph = Graph()
    graph.d = {'A': {'B': 1, 'C': 2},
               'B': {'C': 2},
               'C': {'D': 3, 'E': 5},
               'D': {},
               'E': {'B': 7}}
    return graph


@pytest.fixture(scope="function")
def complex_cyclic():
    graph = Graph()
    graph.d = {'A': {'B': 1, 'C': 4},
               'B': {'C': 2, 'D': 4, 'E': 11},
               'C': {'F': 5, 'G': 3},
               'D': {},
               'E': {},
               'F': {'B': 8},
               'G': {}}
    return graph


@pytest.fixture(scope="function")
def shortest_dead_end():
    graph = Graph()
    graph.d = {'A': {'B': 20, 'C': 3},
               'B': {},
               'C': {'D': 2, 'E': 1},
               'D': {'F': 4},
               'E': {},
               'F': {'B': 5}}
    return graph


@pytest.fixture(scope="function")
def shortest_wiki():
    graph = Graph()
    graph.d = {'A': {'B': 4, 'C': 2},
               'B': {'C': 5, 'D': 10},
               'C': {'E': 3},
               'D': {'F': 11},
               'E': {'D': 4},
               'F': {}}
    return graph


@pytest.fixture(scope="function")
def neg_wt():
    graph = Graph()
    graph.d = {'A': {'B': -1, 'C': 4},
               'B': {'C': 3, 'D': 2, 'E': 2},
               'C': {},
               'D': {'B': 1, 'C': 5},
               'E': {'D': -3}}
    return graph


def test_init():
    graph = Graph()
    assert graph.d == {}


def test_nodes(simple_non_cylic):
    graph = simple_non_cylic
    assert graph.nodes() == graph.d.keys()


def test_edges(simple_non_cylic):
    graph = simple_non_cylic
    edges = [(n, e, graph.d[n][e]) for n in graph.d for e in graph.d[n]]
    assert graph.edges() == edges


def test_add_node():
    graph = Graph()
    graph.add_node('A')
    assert graph.d == {'A': {}}


def test_add_node_error():
    graph = Graph()
    graph.add_node('A')
    with pytest.raises(ValueError):
        graph.add_node('A')


def test_add_edge_dne():
    graph = Graph()
    graph.add_edge('B', 'A', 1)
    assert graph.d == {'A': {}, 'B': {'A': 1}}


def test_add_edge(simple_graph):
    graph = simple_graph
    graph.add_edge('B', 'C', 3)
    assert graph.d == {'A': {'B': 1},
                       'B': {'C': 3},
                       'C': {}}


def test_del_node_dne():
    graph = Graph()
    with pytest.raises(KeyError):
        graph.del_node('A')


def test_del_node():
    graph = Graph()
    graph.add_node('A')
    assert 'A' in graph.d
    graph.del_node('A')
    assert 'A' not in graph.d


def test_del_node_edges(simple_graph):
    graph = simple_graph
    graph.del_node('B')
    assert graph.d['A'] == {}


def test_has_node():
    graph = Graph()
    graph.add_node('A')
    assert graph.has_node('A')
    assert graph.has_node('B') is False


def test_neighbors_dne():
    graph = Graph()
    with pytest.raises(KeyError):
        assert graph.neighbors('A') == {}


def test_neighbors(simple_non_cylic):
    graph = simple_non_cylic
    assert graph.neighbors('A') == ['B', 'C']


def test_adjacent_dne():
    graph = Graph()
    graph.add_node('A')
    with pytest.raises(ValueError):
        graph.adjacent('A', 'B')


def test_adjacent(simple_graph):
    graph = simple_graph
    assert graph.adjacent('A', 'B')


def test_not_adjacent(simple_non_cylic):
    graph = simple_non_cylic
    assert not graph.adjacent('A', 'D')


def test_depth_first_non_cyclic_root(simple_non_cylic):
    graph = simple_non_cylic
    for k in ['A', 'B', 'C', 'D', 'E']:
        assert k in graph.depth_first('A')


def test_depth_first_non_cyclic_non_root(simple_non_cylic):
    graph = simple_non_cylic
    assert graph.depth_first('B') == ['B']


def test_depth_first_cyclic_root(simple_cyclic):
    graph = simple_cyclic
    for k in ['A', 'B', 'C', 'D', 'E']:
        assert k in graph.depth_first('A')


def test_depth_first_cyclic_non_root(simple_cyclic):
    graph = simple_cyclic
    for k in ['B', 'C', 'D', 'E']:
        assert k in graph.depth_first('B')


def test_breadth_first_non_cyclic_root(simple_non_cylic):
    graph = simple_non_cylic
    for k in ['A', 'B', 'C', 'D', 'E']:
        assert k in graph.depth_first('A')


def test_breadth_first_non_cyclic_non_root(simple_non_cylic):
    graph = simple_non_cylic
    assert graph.breadth_first('B') == ['B']


def test_breadth_first_cyclic_root(complex_cyclic):
    graph = complex_cyclic
    for k in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        assert k in graph.depth_first('A')


def test_breadth_first_cyclic_non_root(complex_cyclic):
    graph = complex_cyclic
    for k in ['B', 'C', 'D', 'E', 'F', 'G']:
        assert k in graph.depth_first('B')


def test_dijkstra_dead_end(shortest_dead_end):
    graph = shortest_dead_end
    assert graph.dijkstra('A', 'B') == ['A', 'C', 'D', 'F', 'B']


def test_dijkstra_wiki_ex(shortest_wiki):
    graph = shortest_wiki
    assert graph.dijkstra('A', 'F') == ['A', 'C', 'E', 'D', 'F']


def test_dijkstra_complex_cyclic(complex_cyclic):
    graph = complex_cyclic
    assert graph.dijkstra('A', 'G') == ['A', 'B', 'C', 'G']


def test_bellman_ford_dead_end(shortest_dead_end):
    graph = shortest_dead_end
    assert graph.bellman_ford('A', 'B') == ['A', 'C', 'D', 'F', 'B']


def test_bellman_ford_wiki_ex(shortest_wiki):
    graph = shortest_wiki
    assert graph.bellman_ford('A', 'F') == ['A', 'C', 'E', 'D', 'F']


def test_bellman_ford_complex_cyclic(complex_cyclic):
    graph = complex_cyclic
    assert graph.bellman_ford('A', 'G') == ['A', 'B', 'C', 'G']


def test_bellman_ford_neg_wt(neg_wt):
    graph = neg_wt
    assert graph.bellman_ford('A', 'C') == ['A', 'B', 'C']


def test_bellman_ford_neg_wt_alt_end(neg_wt):
    graph = neg_wt
    assert graph.bellman_ford('A', 'D') == ['A', 'B', 'E', 'D']


def test_bellman_ford_neg_cycle():
    graph = Graph()
    graph.d = {'A': {'B': 3},
               'B': {'C': 4, 'D': -2},
               'C': {},
               'D': {'E': 1},
               'E': {'B': -4}}
    with pytest.raises(Exception):
        graph.bellman_ford('A', 'C')
