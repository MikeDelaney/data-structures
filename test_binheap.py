# -*- charset: utf-8 -*-

import pytest
from binheap import Binheap


@pytest.fixture(scope="function")
def init_list():
    raw = [1, -3, 5, 7, -9]
    min_heap = [-9, -3, 5, 7, 1]
    max_heap = [7, 1, 5, -3, -9]
    return raw, min_heap, max_heap


def test_comp_min():
    heap = Binheap()
    assert heap.comp_min(5, 4) is False
    assert heap.comp_min(-5, -4) is True


def test_comp_max():
    heap = Binheap()
    assert heap.comp_max(5, 4) is True
    assert heap.comp_max(-5, -4) is False


def test_binheap_init_default():
    heap = Binheap()
    assert len(heap._list) == 0
    assert heap.compare == heap.comp_min


def test_binheap_init_max():
    heap = Binheap(minmax='max')
    assert len(heap._list) == 0
    assert heap.compare == heap.comp_max


def test_binheap_init_iter_min(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(raw, minmax="min")
    assert heap._list == min_heap


def test_binheap_init_iter_max(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(raw, minmax="max")
    assert heap._list == max_heap


def test_heapify_min(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(minmax="min")
    heap._list.extend(raw)
    heap._build()
    assert heap._list == min_heap


def test_heapify_max(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(minmax="max")
    heap._list.extend(raw)
    heap._build()
    assert heap._list == max_heap


def test_push_min_large(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(min_heap, minmax="min")
    heap.push(10)
    assert heap._list == [-9, -3, 5, 7, 1, 10]


def test_push_min_small(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(min_heap, minmax="min")
    heap.push(3)
    assert heap._list == [-9, -3, 3, 7, 1, 5]


def test_push_max_small(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(max_heap, minmax="max")
    heap.push(3)
    assert heap._list == [7, 1, 5, -3, -9, 3]


def test_push_max_med(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(max_heap, minmax="max")
    heap.push(6)
    assert heap._list == [7, 1, 6, -3, -9, 5]


def test_push_max_large(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(max_heap, minmax="max")
    heap.push(10)
    assert heap._list == [10, 1, 7, -3, -9, 5]


def test_pop_min(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(raw, minmax="min")
    heap.pop()
    assert heap._list == [-3, 1, 5, 7]


def test_pop_max(init_list):
    raw, min_heap, max_heap = init_list
    heap = Binheap(raw, minmax="max")
    heap.pop()
    assert heap._list == [5, 1, -9, -3]
