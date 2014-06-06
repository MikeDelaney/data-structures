import pytest
from stack import Stack


def test_new_stack():
    stack = Stack()
    assert stack.head is None

def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.head.value == 1
    assert stack.head.next_node is None

    previous_head = stack.head
    stack.push(2)
    assert stack.head.value == 2
    assert stack.head.next_node is previous_head
    assert previous_head.value == 1
    assert previous_head.next_node is None


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    index_1 = stack.head
    stack.push(2)
    index_2 = stack.head
    stack.push(3)

    assert stack.pop() == 3
    assert stack.head is index_2

    assert stack.pop() == 2
    assert stack.head is index_1

    stack.pop()
    assert stack.head is None

    try:
        stack.pop()
    except LookupError:
        pass
    except Exception:
        raise AssertionError("Exception other than LookupError raised")
    else:
        raise AssertionError(
            "No exception raised when when popping from an empty stack"
        )
