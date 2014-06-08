import pytest
from stack import Stack
from stack import Node


@pytest.fixture(scope="function")
def init_test_stack():
    node1 = Node(1, None)
    node2 = Node(2, node1)
    stack = Stack()
    stack.head = node2
    return stack, node1, node2


def test_new_stack():
    stack = Stack()
    assert stack.head is None


def test_stack_push_empty():
    stack = Stack()
    stack.push(1)
    assert stack.head.value == 1
    assert stack.head.next_node is None


def test_stack_push(init_test_stack):
    stack, node1, node2 = init_test_stack
    previous_head = stack.head
    stack.push(3)
    assert stack.head.value == 3
    assert stack.head.next_node is previous_head
    assert previous_head.value == 2


def test_stack_pop(init_test_stack):
    stack, node1, node2 = init_test_stack
    assert stack.pop() == 2
    assert stack.head is node1


def test_stack_pop_head(init_test_stack):
    stack, node1, node2 = init_test_stack
    stack.pop()
    stack.pop()
    assert stack.head is None


def test_stack_pop_empty():
    with pytest.raises(LookupError):
        new_stack = Stack()
        new_stack.pop()
