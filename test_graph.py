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
    edges = []
    for e in graph.values():
        edges.extend(e)

    assert graph.edges() == edges
