# -*- coding: utf-8 -*-

import pytest
from priorityq import Priorityq
from priorityq import Item


@pytest.fixture(scope="function")
def init_list():
    raw = [Item(1, 500), Item(-3, u"Bob"), Item(5, "Fred"),
           Item(7, 600), Item(-9, 700)]
    min_heap = [-9, -3, 5, 7, 1]
    max_heap = [7, 1, 5, -3, -9]
    return raw, min_heap, max_heap


def test_init_item_defaults():
    item = Item()
    assert item.priority == 0
    assert item.value == None


def test_init_item():
    item = Item(1, u"Hey")
    assert item.priority == 1
    assert item.value == u"Hey"


def test_init_cmp():
    item1 = Item(2, u"Bob")
    item2 = Item(0, u"Fred")
    assert item2 > item1


# def test_init_priorityq():
#     q = Priorityq()
#     assert q == []


def test_priorityq_pop():
    q = Priorityq()
    
