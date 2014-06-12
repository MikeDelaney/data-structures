# -*- coding: utf-8 -*-

from priorityq import priorityq
from priorityq import Item

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
