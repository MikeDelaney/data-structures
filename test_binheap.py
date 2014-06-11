# -*- charset: utf-8 -*-

import pytest
from binheap import binheap


@pytest.fixture(scope="function")
def init_list():
    raw = [1, -3, 5, 7, -9]
    min_heap = [-9, -3, 5, 7, 1]
    max_heap = [7, 5, 1, -3, -9]
    return raw, min_heap, max_heap


def test_comp_min():
    heap = binheap()
    assert heap.comp_min(5, 4) is False
    assert heap.comp_min(-5, -4) is True


def test_comp_max():
    heap = binheap()
    assert heap.comp_max(5, 4) is True
    assert heap.comp_max(-5, -4) is False


def test_binheap_init_default():
    heap = binheap()
    assert len(heap) == 0
    assert heap.compare is binheap.comp_max


def test_binheap_init_iter_min(init_list):
    raw, min_heap, max_heap = init_list
    heap = binheap(raw, minmax="min")
    assert heap == min_heap


def test_binheap_init_iter_max(init_list):
    raw, min_heap, max_heap = init_list
    heap = binheap(raw, minmax="max")
    assert heap == max_heap
