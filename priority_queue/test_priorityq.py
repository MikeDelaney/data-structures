# -*- coding: utf-8 -*-

import pytest
from priorityq import Priorityq
from priorityq import Item


@pytest.fixture(scope="function")
def init_list():
    return [Item(1, 500), Item(-3, u"Bob"), Item(5, u"Fred"),
            Item(7, 600), Item(-9, 700)]


def test_init_item():
    item = Item(1, u"Hey")
    assert item.priority == 1
    assert item.value == u"Hey"


def test_init_cmp():
    item1 = Item(2, u"Bob")
    item2 = Item(0, u"Fred")
    assert item1 > item2


def test_pop(init_list):
    q = Priorityq(init_list)
    q.pop()
    assert [x.priority for x in q] == [-3, 1, 5, 7]


def test_insert_empty():
    q = Priorityq()
    q.insert(2, u'octopus')
    assert q == [Item(2, u'octopus')]


def test_insert(init_list):
    q = Priorityq(init_list)
    q.insert(3, u'dog')
    assert [x.priority for x in q] == [-9, -3, 3, 7, 1, 5]


def test_peek(init_list):
    q = Priorityq(init_list)
    assert q.peek() == 700
    assert [x.priority for x in q] == [-9, -3, 5, 7, 1]
