# -*- charset: utf-8 -*-

import pytest
from graph import Graph


@pytest.fixture(scope="function")
def simple_graph():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')
    return graph


@pytest.fixture(scope="function")
def simple_non_cylic():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    return graph


@pytest.fixture(scope="function")
def simple_cyclic():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'B')
    return graph


@pytest.fixture(scope="function")
def complex_cyclic():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_node('G')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('C', 'G')
    graph.add_edge('F', 'B')
    return graph


def test_init():
    graph = Graph()
    assert graph.d == {}


def test_nodes():
    graph = Graph()
    graph.d = {node: edges for (node, edges) in
               [(hashable, []) for hashable in range(10)]
               }
    assert graph.nodes() == graph.d.keys()


def test_edges():
    graph = Graph()
    graph.d = {node: edges for (node, edges) in
               [(hashable, range(10)) for hashable in range(10)]
               }
    edges = [(n, e) for n in graph.d for e in graph.d[n]]
    assert graph.edges() == edges


def test_add_node():
    graph = Graph()
    graph.add_node('A')
    assert graph.d == {'A': []}


def test_add_node_errpr():
    graph = Graph()
    graph.add_node('A')
    with pytest.raises(ValueError):
        graph.add_node('A')


def test_add_edge_dne():
    graph = Graph()
    graph.add_edge('B', 'A')
    assert graph.d == {'A': [], 'B': ['A']}


# def test_add_edge(simple_graph):
#     graph = simple_graph
# noticed this test does nothing, will fix later...

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
    assert graph.d['A'] == []


def test_has_node():
    graph = Graph()
    graph.add_node('A')
    assert graph.has_node('A')
    assert graph.has_node('B') is False


def test_neighbors_dne():
    graph = Graph()
    with pytest.raises(ValueError):
        assert graph.neighbors('A') == []


def test_neighbors():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_edge('B', 'A')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    assert graph.neighbors('B') == ['A', 'C', 'D']


def test_adjacent_dne():
    graph = Graph()
    graph.add_node('A')
    with pytest.raises(ValueError):
        graph.adjacent('A', 'B')


def test_adjacent(simple_graph):
    graph = simple_graph
    assert graph.adjacent('A', 'B')


def test_not_adjacent():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_edge('A', 'C')
    assert not graph.adjacent('A', 'B')


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
