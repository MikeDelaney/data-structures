import pytest
from dll import Dll, Node


def test_init_node():
    new_node = Node()
    assert new_node.prev is None
    assert new_node.next_node is None
    assert new_node.value is None


def test_init_dll():
    dll = Dll()
    assert dll.head is None
    assert dll.tail is None


def test_insert_empty():
    dll = Dll()
    dll.insert(500)
    assert dll.head.prev is None
    assert dll.head.next_node is None
    assert dll.head.value == 500
    assert dll.head is dll.tail


def test_insert():
    dll = Dll()
    dll.insert(500)
    first_node = dll.head
    dll.insert(600)
    assert dll.head.next_node is first_node
    assert dll.head.prev is None
    assert dll.head.value == 600
    assert dll.tail.prev is dll.head


def test_append_empty():
    dll = Dll()
    dll.append(500)
    assert dll.head.prev is None
    assert dll.head.next_node is None
    assert dll.head.value == 500
    assert dll.head is dll.tail


def test_append():
    dll = Dll()
    dll.append(500)
    first_node = dll.tail
    dll.append(600)
    assert dll.tail.prev is first_node
    assert dll.tail.next_node is None
    assert dll.tail.value == 600
    assert dll.head.next_node is dll.tail


def test_pop_empty():
    dll = Dll()
    with pytest.raises(LookupError):
        dll.pop()


def test_pop():
    dll = Dll()
    dll.append(500)
    dll.append(600)
    assert dll.pop() == 500
    assert dll.head.prev is None


def test_shift_empty():
    dll = Dll()
    with pytest.raises(LookupError):
        dll.shift()


def test_shift():
    dll = Dll()
    dll.append(500)
    dll.append(600)
    assert dll.shift() == 600
    assert dll.tail.next_node is None


def test_remove_empty():
    dll = Dll()
    with pytest.raises(LookupError):
        dll.remove(500)


def test_remove_not_found():
    dll = Dll()
    dll.append(600)
    dll.insert(700)
    with pytest.raises(LookupError):
        dll.remove(500)


def test_remove_head():
    dll = Dll()
    dll.append(500)
    dll.append(600)
    dll.append(700)
    dll.remove(500)
    assert dll.head.value == 600
    assert dll.head.next_node is dll.tail
    assert dll.head.prev is None


def test_remove_tail():
    dll = Dll()
    dll.insert(500)
    dll.insert(600)
    dll.insert(700)
    dll.remove(500)
    assert dll.tail.value == 600
    assert dll.tail.prev is dll.head
    assert dll.tail.next_node is None


def test_remove():
    dll = Dll()
    dll.insert(500)
    dll.insert(600)
    back = dll.head
    dll.insert(700)
    dll.insert(800)
    front = dll.head
    dll.insert(900)
    dll.remove(700)
    assert back.prev is front
    assert front.next_node is back
