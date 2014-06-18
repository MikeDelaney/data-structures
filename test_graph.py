# -*- charset: utf-8 -*-

import pytest
from graph import Graph


def test_g_init():
    graph = Graph()
    assert graph.d == {}


def test_g_nodes():
    graph = Graph()
    graph.d = {node: edges for (node, edges) in
               [(hashable, []) for hashable in range(10)]
               }
    assert graph.nodes() == graph.d.keys()


def test_g_edges():
    graph = Graph()
    graph.d = {node: edges for (node, edges) in
               [(hashable, range(10)) for hashable in range(10)]
               }
    edges = [e for n in graph.d for e in graph.d[n]]
    assert graph.edges() == edges


def test_g_add_node():
    graph = Graph()
    graph.add_node('A')
    assert graph.d == {'A': []}

def test_g_add_edge_dne():
    graph = Graph()
    graph.add_edge('B', 'A')
    assert graph.d == {'A': [], 'B': ['A']}


def test_g_add_edge():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')


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

def test_del_node_edges():
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_edge('A', 'B')
    graph.del_node('B')
    assert graph.d['A'] == []
