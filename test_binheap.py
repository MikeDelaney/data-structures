# -*- charset: utf-8 -*-

from binheap import binheap


def test_comp_min():
    assert binheap.compmin(5, 4) is False
    assert binheap.compmin(-5, -4) is True


def test_comp_max():
    assert binheap.compmax(5, 4) is True
    assert binheap.compmax(-5, -4) is False



