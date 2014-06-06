# -*- coding: utf-8 -*-
import pytest
from linked_list import linked_list
from linked_list import node


@pytest.fixture(scope='function')
def build_empty_list():
    return linked_list()


@pytest.fixture(scope='function')
def build_populated_list():
    item5 = node(1, None)
    item4 = node('dog', item5)
    item3 = node(45, item4)
    item2 = node('octopus', item3)
    item1 = node(37, item2)
    populated_list = linked_list()
    populated_list.head = item1
    return populated_list, item1, item2, item3, item4, item5


def test_linked_list(build_empty_list):
    empty_list = build_empty_list
    assert empty_list.head is None


def test_insert(build_empty_list, build_populated_list):
    empty_list = build_empty_list
    populated_list, item1, item2, item3, item4, item5 = build_populated_list
    new_item = node('new', None)
    empty_list.insert(new_item)
    assert new_item.next_node is None
    assert empty_list.head == new_item
    populated_list.insert(new_item)
    assert new_item.next_node == item1
    assert populated_list.head == new_item


def test_pop(build_empty_list, build_populated_list):
    empty_list = build_empty_list
    populated_list, item1, item2, item3, item4, item5 = build_populated_list
    assert empty_list.pop() is None
    actual_populated = populated_list.head.value
    expected_populated = item1.value
    assert actual_populated == expected_populated
    assert populated_list.head == item2


def test_size(build_empty_list, build_populated_list):
    empty_list = build_empty_list
    populated_list, item1, item2, item3, item4, item5 = build_populated_list
    assert empty_list.size() == 0
    assert populated_list.size() == 5


def test_search(build_empty_list, build_populated_list):
    empty_list = build_empty_list
    populated_list, item1, item2, item3, item4, item5 = build_populated_list
    assert empty_list.search(7) is None
    assert populated_list.search(7) is None
    assert populated_list.search(37) == item1
    assert populated_list.search('octopus') == item2
    assert populated_list.search(1) == item5


def test_remove(build_populated_list):
    populated_list, item1, item2, item3, item4, item5 = build_populated_list
    assert populated_list.remove(item1).search(item1) is None
    assert populated_list.remove(item3).search(item3) is None
    assert populated_list.remove(item5).search(item5) is None


def test_print(build_empty_list, build_populated_list):
    empty_list = build_empty_list
    populated_list, item1, item2, item3, item4, item5 = build_populated_list
    assert str(empty_list) == '()'
    assert str(populated_list) == "(37, 'octopus', 45, 'dog', 1)"
