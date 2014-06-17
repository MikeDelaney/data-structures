# -*- charset: utf-8 -*-

import pytest

def test_g_nodes():
    graph = {node: edges for (node, edges) in \
             [(hashable, []) for hashable in range(10)]
             }
    assert graph.nodes() == graph.keys()


