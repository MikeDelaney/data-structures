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
    graph.d = {'A': {'B': 1, 'C': 2},
               'B': {'C': 2},
               'C': {'F': 5, 'G': 3},
               'D': {},
               'E': {},
               'F': {'B': 8},
               'G': {}}
    return graph


def test_init():
    graph = Graph()
    assert graph.d == {}


def test_nodes(simple_non_cylic):
    graph = simple_non_cylic
    assert graph.nodes() == graph.d.keys()


def test_edges(simple_non_cylic):
    graph = simple_non_cylic
    # watch this one
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
    graph.add_edge('B', 'A')
    assert graph.d == {'A': {}, 'B': {'A': 1}}


def test_add_edge(simple_graph):
    graph = simple_graph
    graph.d = {'A': {'B': 1},
               'B': {}}
    graph.add_edge('B', 'C', 3)
    assert graph.d == {'A': {'B': 1},
                       'B': {'C': 3}}


def test_del_node_dne():
    graph = Graph()
    with pytest.raises(ValueError):
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
    with pytest.raises(ValueError):
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
    assert graph.depth_first('A') == ['A', 'B', 'C', 'D', 'E']


def test_depth_first_non_cyclic_non_root(simple_non_cylic):
    graph = simple_non_cylic
    assert graph.depth_first('B') == ['B']


def test_depth_first_cyclic_root(simple_cyclic):
    graph = simple_cyclic
    assert graph.depth_first('A') == ['A', 'B', 'C', 'D', 'E']


def test_depth_first_cyclic_non_root(simple_cyclic):
    graph = simple_cyclic
    assert graph.depth_first('B') == ['B', 'C', 'D', 'E']


def test_breadth_first_non_cyclic_root(simple_non_cylic):
    graph = simple_non_cylic
    assert graph.breadth_first('A') == ['A', 'B', 'C', 'D', 'E']


def test_breadth_first_non_cyclic_non_root(simple_non_cylic):
    graph = simple_non_cylic
    assert graph.breadth_first('B') == ['B']


def test_breadth_first_cyclic_root(complex_cyclic):
    graph = complex_cyclic
    assert graph.breadth_first('A') == ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def test_breadth_first_cyclic_non_root(complex_cyclic):
    graph = complex_cyclic
    assert graph.breadth_first('B') == ['B', 'C', 'D', 'E', 'F', 'G']
