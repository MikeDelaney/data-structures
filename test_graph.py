# -*- charset: utf-8 -*-

import pytest


def test_g_nodes():
    graph = {node: edges for (node, edges) in
             [(hashable, []) for hashable in range(10)]
             }
    assert graph.nodes() == graph.keys()


def test_g_edges():
    graph = {node: edges for (node, edges) in
             [(hashable, range(10)) for hashable in range(10)]
             }
    edges = [e for n in graph for e in graph[n]]
    assert graph.edges() == edges
