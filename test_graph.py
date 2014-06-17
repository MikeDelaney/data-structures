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
